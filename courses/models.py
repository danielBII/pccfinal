from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Courses(models.Model):
    title = RichTextUploadingField()
    text = RichTextUploadingField()
    slug = models.SlugField(null=True, unique=True)
    img = models.ImageField(upload_to="posts/")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title