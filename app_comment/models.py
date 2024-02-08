from django.db import models
from app_blog.models import Post_list

from django.utils import timezone
from app_clients.models import Client


class Comment(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    post_list = models.ForeignKey(Post_list, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.user} on {self.post_List.title}, {self.id}"
