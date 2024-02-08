from rest_framework import serializers
from .models import Comment
from drf_spectacular.utils import extend_schema_field


class CommentSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField()
    avatar_url = serializers.SerializerMethodField()

    @extend_schema_field(str)
    def get_avatar_url(self, obj):
        return obj.user.avatar.url if obj.user.avatar else None




    class Meta:
        model = Comment
        fields = ['id', 'post_list', 'user', 'avatar_url', 'text', 'created_date']