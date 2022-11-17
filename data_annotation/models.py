from django.db import models

# Create your models here.

from data_collection.models import Image


class DataAnnotation(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    ocr_text = models.TextField()

    def save(self, *args, **kwargs):
        self.image.is_ocred = True
        self.image.save()
        super(DataAnnotation, self).save(*args, **kwargs)
