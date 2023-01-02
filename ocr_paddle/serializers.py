from rest_framework import serializers
from .models import Ocrdata


class OcrModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocrdata
        fields = '__all__'
