from django.db import models

# Create your models here.


class Ocrdata(models.Model):
    image = models.ImageField(upload_to="ocr/uploads")
    result = models.TextField(blank=True)
