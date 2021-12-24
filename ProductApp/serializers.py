from rest_framework import serializers

from ProductApp.models import ProductModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        exclude = ('is_active', )
