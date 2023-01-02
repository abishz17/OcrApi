from django.db import models

# Create your models here.


class FeedBack(models.Model):
    email = models.EmailField(blank=True)
    description = models.TextField()
