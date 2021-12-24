from rest_framework import serializers

from ProductApp.models import ProductModel
from StatusApp.models import (StatusTypeModel, PriorityTypeModel, ProblemTypeModel)


class StatusTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTypeModel
        fields = '__all__'


class PriorityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriorityTypeModel
        fields = '__all__'


class ProblemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemTypeModel
        fields = '__all__'
