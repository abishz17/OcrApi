from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import AnnotationSerializer
from data_collection.serializers import ImageSerializer
from .models import DataAnnotation
from data_collection.models import Image


class AnnotationView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, id):
        image = Image.objects.get(id=id)
        image_serializer = ImageSerializer(image, many=False)
        return Response(image_serializer.data["image"], status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        entries_serializer = AnnotationSerializer(data=request.data)
        if entries_serializer.is_valid():
            entries_serializer.save()
            return Response(entries_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('errors', entries_serializer.errors)
            return Response(entries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
