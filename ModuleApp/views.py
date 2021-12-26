from rest_framework import viewsets, mixins, filters, status
from rest_framework.permissions import IsAuthenticated, AllowAny

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .filters import SubSystemFilter
from .models import SubSystemModel, ModuleModel
from .serializers import SubSystemSerializer, ModuleSerializer, SubSystemDetailSerializer, \
    SubSystemCreateUpdateSerializer, ModuleCreateUpdateSerializer


class SubSystemViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = SubSystemModel.objects.all()
    serializer_class = SubSystemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = SubSystemFilter
    search_fields = ['product__title', 'title', 'description']
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return SubSystemSerializer
        elif self.action in ('retrieve', 'partial_retrieve'):
            return SubSystemDetailSerializer
        elif self.action in ('update', 'partial_update', 'create'):
            return SubSystemCreateUpdateSerializer
        return SubSystemSerializer


class FiltersViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = SubSystemModel.objects.all()
    serializer_class = SubSystemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = SubSystemFilter
    search_fields = ['product__title', 'title', 'description']
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return SubSystemSerializer
        elif self.action in ('retrieve', 'partial_retrieve'):
            return SubSystemDetailSerializer
        return SubSystemSerializer


class ModuleViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = ModuleModel.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action in ('update', 'partial_update', 'create'):
            return ModuleCreateUpdateSerializer
        return ModuleSerializer

    def get_queryset(self):
        return ModuleModel.objects.filter(subsystemmodel=self.kwargs['systemID'])

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        system = SubSystemModel.objects.filter(id=self.kwargs['systemID']).first()
        system.modules.add(serializer.data['id'])
        system.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)