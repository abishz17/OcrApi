from django.urls import path
from .views import OcrView, upload
from django.views.decorators.http import require_POST

urlpatterns = [
    path('api/', OcrView, name='ocrview'),
    path('upload/', upload, name='upload'),
]
