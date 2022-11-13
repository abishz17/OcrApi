from django.urls import path
from .views import OcrView, ImageView

urlpatterns = [
    path('api/', OcrView.as_view(), name='ocrview'),
    path('image/', ImageView.as_view(), name='image'),
]
