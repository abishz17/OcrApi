from django.urls import path
from .views import AnnotationView

urlpatterns = [
    path('image/', AnnotationView.as_view(), name='image'),
   # path('getdata',get_data,name='get')
]
