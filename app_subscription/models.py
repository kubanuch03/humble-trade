from django.db import models
from app_users.models import CustomUser


class Subscription(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_subscribed = models.BooleanField(default=False)
    expiration_date = models.DateTimeField(null=True, blank=True)
