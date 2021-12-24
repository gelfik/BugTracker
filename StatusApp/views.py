from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import StatusTypeModel, ProblemTypeModel, PriorityTypeModel
from .serializers import StatusTypeSerializer, ProblemTypeSerializer, PriorityTypeSerializer


class StatusViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = StatusTypeModel.objects.all()
    serializer_class = StatusTypeSerializer
    permission_classes = (AllowAny,)


class ProblemViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = ProblemTypeModel.objects.all()
    serializer_class = ProblemTypeSerializer
    permission_classes = (AllowAny,)


class PriorityViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = PriorityTypeModel.objects.all()
    serializer_class = PriorityTypeSerializer
    permission_classes = (AllowAny,)
