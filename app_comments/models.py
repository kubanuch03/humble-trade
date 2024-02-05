from django.db import models
from app_video_library.models import Courses
from app_resourse_center.models import Document
from app_clients.models import Client
from django.shortcuts import render


class CommentCourse(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    post = models.ForeignKey(Courses, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.user.avatar} {self.id}"


class CommentDocument(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    post = models.ForeignKey(Document, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.user.avatar} {self.id}"
