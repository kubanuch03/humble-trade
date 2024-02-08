# Ваш файл forms.py
from django.contrib.auth.forms import UserCreationForm
from app_clients.models import Client

class ClientCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Client
        fields = ('email', 'username',)  # Добавьте другие поля, если необходимо
