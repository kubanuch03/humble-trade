from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import login, authenticate
from django.utils import timezone
from datetime import timedelta

from .models import Client
from .permissions import IsClientOrAdmin
from .serializers import ClientSerializer, LoginClientSerializer, ConfirmEmailSerializer

import time


class LoginClientView(generics.GenericAPIView):
    serializer_class = LoginClientSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        if email and password:
            client = authenticate(username=email, password=password)
            print(f"Client: {client}")

            if client:
                login(request, client)
                refresh = RefreshToken.for_user(client)
                return Response(
                    {
                        "user_id": client.id,
                        "email": client.email,
                        "username": client.username,
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "detail": "Authentication failed. User not found or credentials are incorrect."
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"detail": "Invalid input. Both email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, token):
        try:
            user = Client.objects.get(activation_token=token)
            user.is_active = True
            user.save()
        except Client.DoesNotExist:
            raise ({"error": "invalid-token"})


class ConfirmEmailView(generics.GenericAPIView):
    serializer_class = ConfirmEmailSerializer

    @staticmethod
    def get(request, token):
        try:
            user = Client.objects.get(token_auth=token)
            if user.is_active:
                return Response(
                    {"detail": "User is already activated"}, status=status.HTTP_200_OK
                )

            user.is_active = True
            user.save()

            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "detail": "Email confirmation successful",
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,
            )

        except Client.DoesNotExist:
            return Response(
                {"detail": "Invalid token"}, status=status.HTTP_404_NOT_FOUND
            )


class RegisterClientView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        print("Before perform_create")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = serializer.save()

        print("After perform_create")
        return Response(
            {
                "detail": "Registration successful",
                "user_id": client.id,
                "email": client.email,
                "username": client.username,
            },
            status=status.HTTP_201_CREATED,
        )


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser]


class ClientDeleteView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser]
