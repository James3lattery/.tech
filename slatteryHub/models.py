from django.db import models
from datetime import date


class note(models.Model):
    owner = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    postDate = models.DateField(default=date.today)
    content = models.TextField(max_length=1000)
    pinned = models.BooleanField(default=False)


class file(models.Model):
    owner = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="/media/")


class image(models.Model):
    owner = models.CharField(max_length=100)
    image = models.ImageField()
