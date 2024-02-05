from celery import shared_task
from app_clients.models import Client
from datetime import timedelta
from django.utils import timezone
import threading
import logging

logger = logging.getLogger(__name__)


@shared_task
def delete_user_annually():
    try:
        logger.info("Присступаем к деактивации")
        one_minute_ago = timezone.now() - timezone.timedelta(minutes=30)
        users_to_deactivate = Client.objects.filter(created_at__lt=one_minute_ago)

        for user in users_to_deactivate:
            user.is_active = False
            user.is_client = False
            user.save()
            user.delete()
            logger.info("User deactivated")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
