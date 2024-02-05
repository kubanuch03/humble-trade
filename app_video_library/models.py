from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="video_library/category/")

    def __str__(self):
        return str(f"{self.title}")


class Courses(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="video_library/course/")
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.title}")