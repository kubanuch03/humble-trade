from django.db import models
from transliterate import slugify



class Category(models.Model):
    title = models.CharField(max_length=250,unique=True)
    image = models.ImageField(upload_to='resourse/category')

    

    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField('resourse/document')
    post = models.FileField()
    url = models.URLField()
    description = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.id}"
