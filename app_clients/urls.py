from django.urls import path, include
from .views import *


app_name = "clients"
urlpatterns = [
    path("list/client/", ClientListView.as_view(), name="list_client"),
    path("delete/client/<int:pk>/", ClientDeleteView.as_view(), name="delete_client"),
    path("register/client/", RegisterClientView.as_view(), name="register_client"),
    path("login/client/", LoginClientView.as_view(), name="login_client"),
    path(
        "confirm-email/<str:token>/", ConfirmEmailView.as_view(), name="confirm_email"
    ),
]
