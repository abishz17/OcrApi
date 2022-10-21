from rest_framework import serializers
from .models import Image, Ocred

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class OcrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocred
        fields = ('image','ocr_text')
    image = ImageSerializer(many=False)