from django.urls import path
from .views import OcrView, upload

urlpatterns = [
    path('api/', OcrView.as_view(), name='ocrview'),
    path('upload/', upload, name='upload'),
]
