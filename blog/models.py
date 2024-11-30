# models.py
from django.db import models

class Artwork(models.Model):
    image = models.ImageField(upload_to='artworks/')  # 图片上传路径

    def __str__(self):
        return f"Artwork {self.id}"


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)  # 上传文章图片
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title