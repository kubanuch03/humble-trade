from rest_framework import generics, permissions
from django.utils import timezone
from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionView(generics.RetrieveUpdateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        obj, created = Subscription.objects.get_or_create(user=user)
        return obj

    def perform_update(self, serializer):
        serializer.save(expiration_date=timezone.now() + timezone.timedelta(days=30))
