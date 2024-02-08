from django.db import models
from app_clients.models import Client


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return self.title




class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post_list(models.Model):
    user = models.ManyToManyField(Client)
    hashtags = models.ManyToManyField(Hashtag)
    post = models.ForeignKey(Post, blank=False, related_name="Post", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video = models.URLField()
    
    def __str__(self):
        return f"{self.title} {self.post}"




class Module(models.Model):
    post_list = models.ForeignKey(Post_list, on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to="module/")


    def __str__(self):
        return f"{self.title}, {self.post_list}"