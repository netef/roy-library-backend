from datetime import datetime
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=30)
    available_copies = models.IntegerField()
    date_added = models.DateTimeField(default=datetime.now(), blank=True)
    img_url = models.CharField(max_length=255)
