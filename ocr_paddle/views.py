from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .serializers import OcrModelSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Ocrdata
# Create your views here.


class OCRData(APIView):
    def get(self, request):
        ocr_entries = Ocrdata.objects.all()
        serializer = OcrModelSerializer(ocr_entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data["image"])
        ocr_serializers = OcrModelSerializer(data=request.data)
        result = "Hello How are you"
        if ocr_serializers.is_valid():
            ocr_serializers.save()
            return Response(result, status=status.HTTP_201_CREATED)
        else:
            print('errors', ocr_serializers.errors)
            return Response(ocr_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
