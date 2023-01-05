from django.db import models

# Create your models here.


class FeedBack(models.Model):
    name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    description = models.TextField()
