from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
    path("course/list/", CourseListView.as_view()),
    path("course/create/", CourseListCreateAPIView.as_view()),
    path("course/rud/<int:pk>/", CourseRetrieveUpdateDestroyAPIView.as_view()),
    path("course/detail/<int:pk>/", CourseDetailView.as_view()),
]