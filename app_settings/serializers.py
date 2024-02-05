from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_decode

from rest_framework import serializers
from app_clients.models import Client


class ClientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
            "username",
            "full_name",
            "bio",
            "location",
            "phone_number",
            "address",
            "address_line2",
            "city",
            "state",
            "country",
            "zip",
            "tax_id",
            "facebook",
            "instogram",
            "twitter",
        ]


class RequestPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ["email"]


class ResetPasswordConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        uidb64 = self.context.get("uidb64")
        token = self.context.get("token")

        if not uidb64 or not token:
            raise serializers.ValidationError(
                {
                    "error": "Отсутствуют необходимые параметры в ссылке для сброса пароля"
                }
            )

        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(Client, pk=uid)

        if not default_token_generator.check_token(user, token):
            raise serializers.ValidationError(
                {"error": "Недействительная ссылка для сброса пароля"}
            )

        password = data.get("password")
        password2 = data.get("password2")

        if password != password2:
            raise serializers.ValidationError({"error": "Пароли не совпадают"})

        return data

    def save(self):
        uidb64 = self.context.get("uidb64")
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(Client, pk=uid)

        password = self.validated_data["password"]
        user.set_password(password)
        user.save()
