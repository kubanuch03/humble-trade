from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Review
from .serializers import ReviewSerializer

from drf_spectacular.utils import extend_schema


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    @extend_schema(
        summary="List a  reviews ",
        description="List a  reviews ",
        request=ReviewSerializer,
        responses={200: ReviewSerializer},
        operation_id="list_review_v1",
    )
    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data)
