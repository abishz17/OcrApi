from django.urls import path
from .views import OcrView

urlpatterns = [
    path('',OcrView.as_view(), name='ocrview'),
]