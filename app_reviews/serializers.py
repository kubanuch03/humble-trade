from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(
        source="client.username", allow_null=True, read_only=True
    )
    client_photo = serializers.ImageField(
        source="client.avatar", allow_null=True, read_only=True
    )

    def get_client_name(self, obj):
        return obj.client.username if obj.client else None

    def get_client_photo(self, obj):
        return (
            obj.client.avatar.url
            if obj.client and hasattr(obj.client, "avatar")
            else None
        )

    class Meta:
        model = Review
        fields = ["id", "client", "client_name", "client_photo", "text", "created_at"]
