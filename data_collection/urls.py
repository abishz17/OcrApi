from django.urls import path
from .views import OcrView, upload, OCRGet, get_data
from django.views.decorators.http import require_POST

urlpatterns = [
    path('api/', OcrView, name='ocrview'),
    path('upload/', upload, name='upload'),
    path('viewdata/', OCRGet, name='viewdata'),
    path('migrate/', get_data, name='get')
]
