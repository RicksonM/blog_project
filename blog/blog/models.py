from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=50000)
    caption = models.TextField()
    img_cover = models.CharField(max_length=800)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title