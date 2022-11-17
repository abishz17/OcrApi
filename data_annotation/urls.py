from django.urls import path
from .views import AnnotationView

urlpatterns = [
    path('image/<id>', AnnotationView.as_view(), name='image')
]
