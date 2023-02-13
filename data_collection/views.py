from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework import status
from .serializers import OCR_dataSerializer
from .models import Image, Ocr_data
from rest_framework.decorators import api_view

from django.views.decorators.http import require_POST
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.decorators import parser_classes
from PIL import Image
import os
from django.core.files import File

# class OcrView(APIView):
#     parser_classes = [MultiPartParser, FormParser]
# serializer_class = ImageSerializer
# # queryset = Image.objects.all()
# authentication_classes = [authentication.SessionAuthentication]
# permission_classes = [permissions.IsAdminUser]
# #renderer_classes = [JSONRenderer]

# # def get(self, request, *args, **kwargs):
# #     entries = Image.objects.all()
# #     serializer = ImageSerializer(entries, many=True)
# #     return Response(serializer.data)


@require_POST
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def OcrView(request):
    entries_serializer = OCR_dataSerializer(data=request.data)
    print(entries_serializer)
    if entries_serializer.is_valid():
        entries_serializer.save()
        return Response(entries_serializer.data, status=status.HTTP_201_CREATED)
    else:
        print('errors', entries_serializer.errors)
        return Response(entries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@staff_member_required
def OCRGet(request):
    def get_total_lines(generative_get):
        total_lines = 0
        for lines in generative_get:
            if lines.lines != None:
                total_lines += lines.lines
        return total_lines
    if request.method == 'GET':
        generative_get = Ocr_data.objects.all()
        lines = get_total_lines(generative_get)
        context = {'generative_get': generative_get,
                   "total_lines": lines}
        return render(request, 'data_annoated.html', context=context)


def get_data(request):
    objects = Ocr_data.objects.all()
    folder = '/home/beeps/Desktop/Major/backend/data_collection/migrate'
    for obj in objects:
        if obj.image:
            image_path = os.path.join(folder, str(obj.id) + '.jpg')
            label_path = os.path.join(folder, str(obj.id) + '.txt')
            with open(image_path, 'wb') as f:
                f.write(obj.image.read())
            with open(label_path, 'w') as f:
                f.write(obj.label)
    return HttpResponse("<p>It was a success </p>")


def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            Image.objects.create(image=image)
    images = Image.objects.all()
    return render(request, 'imageupload.html', {'images': images})
