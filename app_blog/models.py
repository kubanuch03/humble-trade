from django.db import models
from transliterate import slugify
from app_clients.models import Client


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    visible_to_users_since = models.DateField(null=True, blank=True)
    visible_to_users = models.ManyToManyField(
        Client, related_name="allowed_posts", blank=True
    )

    def __str__(self):
        return self.title
    



class Hashtag(models.Model):
    name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Post_list(models.Model):
    hashtags = models.ManyToManyField(
        Hashtag,
        related_name="post_lists",
        blank=False,
    )
    post = models.ForeignKey(
        Post, blank=False, related_name="Post", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video = models.URLField()
    visible_to_users_since = models.DateField(null=True, blank=True)
    visible_to_users = models.ManyToManyField(
        Client, related_name="allowed_post_lists",  blank=True
    )

    def __str__(self):
        return f"{self.title} {self.post}"


class Module(models.Model):
    post_list = models.ForeignKey(
        Post_list, related_name="module", on_delete=models.CASCADE,null=True,blank=True
    )
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to="images/")
   

    def __str__(self):
        return f"{self.title}, {self.post_list}"