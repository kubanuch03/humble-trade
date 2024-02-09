from rest_framework import serializers
from .models import CommentCourse, CommentDocument
from drf_spectacular.utils import extend_schema_field
from app_clients.models import Client


class CommentCourseSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    avatar_url = serializers.SerializerMethodField()

    @extend_schema_field(str)
    def get_username(self, obj):
        return obj.user.username if obj.user else None

    @extend_schema_field(str)
    def get_avatar_url(self, obj):
        return obj.user.avatar.url if obj.user.avatar else None
    
    

    class Meta:
        model = CommentCourse
        fields = ["id", "user","username", "avatar_url", "post", "body", "created_at",]


    



class CommentDocumentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    avatar_url = serializers.SerializerMethodField()

    @extend_schema_field(str)
    def get_username(self, obj):
        return obj.user.username if obj.user else None

    @extend_schema_field(str)
    def get_avatar_url(self, obj):
        return obj.user.avatar.url if obj.user.avatar else None

    class Meta:
        model = CommentDocument
        fields = ["id", "user", "avatar_url", "post", "body", "created_at", "username"]
