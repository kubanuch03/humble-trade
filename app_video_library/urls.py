from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")
# router.register(r"courses", CourseViewSet, basename="courses")

urlpatterns = [
    path("", include(router.urls)), 
    path("course/list/create/", CourseListCreateAPIView.as_view()),
    path("course/rud/<int:pk>/", CourseRetrieveUpdateDestroyAPIView.as_view()),
    path("course/list/all/", CourseListView.as_view()),
    path("course/detail/<int:pk>/", CourseListView.as_view()),
]