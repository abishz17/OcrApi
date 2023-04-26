from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework import status
from .serializers import OCR_dataSerializer,ImageSerializer
from .models import Image, Ocr_data
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.decorators import parser_classes

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
class FlagImageView(APIView):
    def post(self, request):
        # Get the image ID from the request data
        image_id = request.data.get('id')
        if not image_id:
            return Response({'error': 'Image ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Get the Image object
        try:
            image = Image.objects.get(pk=image_id)
        except Image.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update the is_flagged field to True
        image.is_flagged = True
        image.save()

        # Serialize the updated Image object and return it in the response
        serializer = ImageSerializer(image)
        return Response(serializer.data)


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
    images = Image.objects.filter(is_ocred=False).filter(is_flagged=False)
    left_images = len(images)
    done_images = Image.objects.filter(is_ocred=True).count()
    flag_count=Image.objects.filter(is_flagged=True).count()
    total_images = Image.objects.all().count()
    paginator = Paginator(images,100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
    'page_obj':page_obj,
    'done_images':done_images,
    'left_images':left_images,
    'flag_count':flag_count,
    'total_images':total_images}
    return render(request, 'imageupload.html', context= context)
