from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = RichTextField()
    text = RichTextUploadingField()
    slug = models.SlugField(null=True, unique=True, blank=True)
    img = models.ImageField(upload_to="posts/")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    public = models.BooleanField(default=True, verbose_name="Anônimo")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title