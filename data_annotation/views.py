from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from .serializers import AnnotationSerializer
from data_collection.serializers import ImageSerializer
from .models import DataAnnotation
#from PIL import Image
from data_collection.models import Image
from rest_framework import authentication, permissions
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

import os

class AnnotationView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    renderer_classes = [JSONRenderer]

    def getImage(self):
        if Image.objects.filter(is_ocred=False).exists():
            image = Image.objects.filter(is_ocred=False).filter(is_flagged=False).order_by('?')[0]
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

#@staff_member_required
#def get_data(request):
    #objects = DataAnnotation.objects.filter()[:1000]
    #folder = 'migrate'
    #label = 'label.txt'
    #iamge_dir = '/home/beeps/Desktop/Major/backend/media/'
    #for obj in objects:
      #  if obj.image:
     #       image_path = os.path.join(folder, str(obj.id) + '.jpg')
           # label_path = os.path.join(folder, str(obj.id) + '.txt')
           # image = Image.open(obj.image.image)
           # image = image.convert('RGB')
           # image.save(image_path,'JPEG')
           # with open(label, 'a') as f:
           #     f.write(str(image_path)+ ' ' + obj.ocr_text + '\n')
    #return HttpResponse("<p>Annotations successfully extracted, look into backend/data_annotation/migrate </p>")
