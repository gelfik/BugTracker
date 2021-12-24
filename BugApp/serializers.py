from rest_framework import serializers

from FilesApp.serializers import FileSerializer
from StatusApp.serializers import PriorityTypeSerializer, ProblemTypeSerializer
from UserProfileApp.serializers import UserDataSerializer
from ProductApp.serializers import ProductSerializer
from .models import BugModel


class BugSerializer(serializers.ModelSerializer):
    user = UserDataSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)
    files = FileSerializer(many=True, read_only=True)
    priority_type = PriorityTypeSerializer(many=False, read_only=True)
    problem_type = ProblemTypeSerializer(many=False, read_only=True)

    class Meta:
        model = BugModel
        # fields = '__all__'
        exclude = ('is_active',)
