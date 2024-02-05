from django.urls import path
from app_resourse_center.views import *


urlpatterns = [
    path("category/create/", CategoryCreateApiView.as_view()),
    path("category/list/", CategoryListApiView.as_view()),
    path("category/delete/<int:pk>/", CategoryDeleteApiView.as_view()),
    path("category/put/<int:pk>/", CategoryPutApiView.as_view()),
    path("category/detail/<int:pk>/", CategoryDetailApiView.as_view()),

    path("document/create/", DocumentCreateApiView.as_view()),
    path("document/list/", DocumentListApiView.as_view()),
    path("document/delete/<int:pk>/", DocumentDeleteApiView.as_view()),
    path("document/put/<int:pk>/", DocumetPutApiView.as_view()),
    path("download/<int:pk>/", DownloadFileView.as_view(), name="download-file"),
]
