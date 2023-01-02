from django.shortcuts import render


from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from rest_framework import status
from .serializers import OCR_dataSerializer
from .models import Image
from rest_framework.decorators import api_view

from django.views.decorators.http import require_POST

from rest_framework.decorators import parser_classes


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


def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist('images')
        for image in images:
            Image.objects.create(image=image)
    images = Image.objects.all()
    return render(request, 'imageupload.html', {'images': images})
