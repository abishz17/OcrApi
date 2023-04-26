from django.urls import path
from .views import OCRData

urlpatterns = [
    path('ocr/', OCRData.as_view(), name='image')
]
