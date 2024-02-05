from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

from .serializers import (
    ClientUpdateSerializer,
    ResetPasswordConfirmSerializer,
    RequestPasswordResetSerializer,
)
from .send_email import send_password_reset_email
from .permissions import IsClientOrAdmin
from app_clients.models import Client

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


class RequestPasswordResetView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RequestPasswordResetSerializer

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        try:
            user = Client.objects.get(email=email)
        except Client.DoesNotExist:
            return Response(
                {"error": "Пользователь с таким email не найден"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        uid = urlsafe_base64_encode(force_str(user.pk).encode())
        token = default_token_generator.make_token(user)

        reset_url = reverse(
            "profile:reset-password-confirm", kwargs={"uidb64": uid, "token": token}
        )
        reset_url = request.build_absolute_uri(reset_url)

        send_password_reset_email(user, reset_url)

        return Response(
            {"success": "Ссылка для восстановления пароля отправлена на ваш email"}
        )


class ResetPasswordConfirmView(generics.GenericAPIView):
    serializer_class = ResetPasswordConfirmSerializer
    permission_classes = [permissions.AllowAny]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={"uidb64": kwargs["uidb64"], "token": kwargs["token"]},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        try:
            serializer.save()
            return Response({"success": "Пароль успешно изменен"})
        except:
            return Response(
                {"error": "Недействительная ссылка для сброса пароля"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ClientUpdateApiView(generics.UpdateAPIView):
    serializer_class = ClientUpdateSerializer
    permission_classes = [IsClientOrAdmin]

    def get_object(self):
        return self.request.user
