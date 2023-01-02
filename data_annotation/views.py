from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .serializers import AnnotationSerializer
from data_collection.serializers import ImageSerializer
from .models import DataAnnotation
from data_collection.models import Image
from rest_framework import authentication, permissions


class AnnotationView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    renderer_classes = [JSONRenderer]

    def getImage(self):
        if Image.objects.filter(is_ocred=False).exists():
            image = Image.objects.filter(is_ocred=False).order_by('?')[0]
            return image
        return False

    def get(self, request):
        if self.getImage() == False:
            return Response("No image available", status=status.HTTP_204_NO_CONTENT)

        image = self.getImage()
        image_serializer = ImageSerializer(image, many=False)
        return Response(image_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        entries_serializer = AnnotationSerializer(data=request.data)
        if entries_serializer.is_valid():
            entries_serializer.save()
            return Response(entries_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(entries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
