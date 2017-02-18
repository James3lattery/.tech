from django.db import models
from datetime import date


class note(models.Model):
    owner = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    postDate = models.DateField(default=date.today)
    content = models.TextField(max_length=1000)
    pinned = models.BooleanField(default=False)
