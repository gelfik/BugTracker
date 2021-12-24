from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from django_filters.rest_framework import DjangoFilterBackend

from .filters import SubSystemFilter
from .models import SubSystemModel, ModuleModel
from .serializers import SubSystemSerializer, ModuleSerializer, SubSystemDetailSerializer, \
    SubSystemCreateUpdateSerializer


class SubSystemViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.CreateModelMixin,
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


class ModuleViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = ModuleModel.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = (AllowAny,)
