from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, ReviewListAPIView

router = DefaultRouter()
router.register(r"reviews", ReviewViewSet, basename="review")

urlpatterns = [
    path("list/reviews/", ReviewListAPIView.as_view(), name="review-list"),
] + router.urls
