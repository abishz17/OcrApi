from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Image(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    image = models.ImageField(upload_to='uploads')
    is_ocred = models.BooleanField(default=False)


class Ocred(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    ocr_text = models.TextField()

    def save(self, *args, **kwargs):
        self.image.is_ocred = True
        self.image.save()
        super(Ocred, self).save(*args, **kwargs)


class Ocr_data(models.Model):
    image = models.ImageField(upload_to='uploads/ocr_data')
    label = models.TextField()
