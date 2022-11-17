from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageSerializer, OcrSerializer, OCR_dataSerializer
from .models import Image, Ocred
# Create your views here.


class OcrView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        entries = Image.objects.all()
        serializer = ImageSerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        entries_serializer = OCR_dataSerializer(data=request.data)
        print(entries_serializer)
        if entries_serializer.is_valid():
            entries_serializer.save()
            return Response(entries_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('errors', entries_serializer.errors)
            return Response(entries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            Image.objects.create(image=image)
    images = Image.objects.all()
    return render(request, 'imageupload.html', {'images': images})
