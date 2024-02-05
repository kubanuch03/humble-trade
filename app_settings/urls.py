from django.urls import path
from .views import *


app_name = "profile"
urlpatterns = [
    path(
        "update/client/<int:pk>/", ClientUpdateApiView.as_view(), name="client_update"
    ),
    path(
        "reset-password/client/",
        RequestPasswordResetView.as_view(),
        name="reset-password",
    ),
    path(
        "reset-password-confirm/client/<str:uidb64>/<str:token>/",
        ResetPasswordConfirmView.as_view(),
        name="reset-password-confirm",
    ),
]
