from django.db import models

# Create your models here.

from data_collection.models import Image
from django.contrib.auth.models import User

class DataAnnotation(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    ocr_text = models.TextField()
   # by=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        self.image.is_ocred = True
        self.image.save()
        super(DataAnnotation, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.ocr_text)

    def natural_key(self):
        return (self.image.natural_key()[0],self.ocr_text)
