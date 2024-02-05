from django.db import models
from app_clients.models import Client


class Review(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.client)
