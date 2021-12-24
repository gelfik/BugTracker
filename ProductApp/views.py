from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import ProductModel
from .serializers import ProductSerializer


class ProductViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
