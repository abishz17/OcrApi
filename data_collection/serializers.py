from rest_framework import serializers
from .models import Image, Ocred, Ocr_data


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'is_ocred')


class OcrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocred
        fields = ('image', 'ocr_text')
    image = ImageSerializer(many=False)


class OCR_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocr_data
        fields = '__all__'
