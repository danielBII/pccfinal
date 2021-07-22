from django.db import models
from django.utils import timezone
import uuid
from django.conf import settings

class Galery(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='galery/')
    description = models.CharField(max_length=150, blank=True)
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)