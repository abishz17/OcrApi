from rest_framework import serializers
from .models import DataAnnotation


class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataAnnotation
        fields = '__all__'
