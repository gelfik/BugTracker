from rest_framework import serializers

from BugApp.serializers import BugSerializer
from StatusApp.serializers import StatusTypeSerializer
from .models import ModuleModel, SubSystemModel
from ProductApp.serializers import ProductSerializer


class ModuleSerializer(serializers.ModelSerializer):
    bugs = BugSerializer(many=True, read_only=True)
    status_type = StatusTypeSerializer(many=False, read_only=True)

    class Meta:
        model = ModuleModel
        exclude = ('is_active',)


class SubSystemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    status_type = StatusTypeSerializer(many=False, read_only=True)

    class Meta:
        model = SubSystemModel
        exclude = ('is_active', 'modules', 'description',)


class SubSystemDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    modules = ModuleSerializer(many=True, read_only=True)
    status_type = StatusTypeSerializer(many=False, read_only=True)

    class Meta:
        model = SubSystemModel
        exclude = ('is_active',)


class SubSystemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubSystemModel
        exclude = ('is_active', 'modules',)


class ModuleCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleModel
        exclude = ('is_active', 'bugs',)
