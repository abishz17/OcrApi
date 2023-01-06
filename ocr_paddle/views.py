from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .serializers import OcrModelSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Ocrdata
from data_collection.serializers import ImageSerializer
from data_annotation.models import Image
from python_folder import main
# Create your views here.


class OCRData(APIView):
    def get(self, request):
        ocr_entries = Ocrdata.objects.all()
        serializer = OcrModelSerializer(ocr_entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        # img = Image.objects.create(image=request.data["image"])
        # result = main.PaddleRun(str(img))
        ocr_serializers = OcrModelSerializer(data=request.data)

        result = "hello"
        print(ocr_serializers)
        if ocr_serializers.is_valid():
            img = ocr_serializers.save()
            result = main.PaddleRun(img.image)
            return Response(result, status=status.HTTP_201_CREATED)
        else:
            print('errors', ocr_serializers.errors)
            return Response(ocr_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
