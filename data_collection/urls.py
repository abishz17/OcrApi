from django.urls import path
from .views import OcrView, upload, OCRGet, get_data, FlagImageView
from django.views.decorators.http import require_POST

urlpatterns = [
    path('api/', OcrView, name='ocrview'),
    path('upload/', upload, name='upload'),
    path('viewdata/', OCRGet, name='viewdata'),
    path('flag', FlagImageView.as_view(), name='flag'),
    #  path('migrate/', get_data, name='get')
]
