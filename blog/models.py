from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-data_added"]
