from django.core.mail import send_mail
from django.conf import settings


def send_password_reset_email(user, reset_url):
    subject = "Восстановление пароля"
    message = f"Для восстановления пароля перейдите по ссылке: {reset_url}"

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
