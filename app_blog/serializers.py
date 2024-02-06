from rest_framework import serializers
from .models import Post, Post_list, Module, Hashtag
from drf_spectacular.utils import extend_schema_field


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","title", "content","visible_to_users_since","visible_to_users"]


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ["name","id"]


class PostListSerializer(serializers.ModelSerializer):
    hashtags = HashtagSerializer(many=True)

    class Meta:
        model = Post_list
        fields = [
            "id",
            "title",
            "description",
            "video",
            "post",
            "hashtags",
            "visible_to_users_since",
            "visible_to_users",
        ]

    @extend_schema_field(str)
    def get_post_title(self, obj):
        return obj.post.title if obj.post else None

    def create(self, validated_data):
        hashtags_data = validated_data.pop("hashtags", None)
        visible_to_users_data = validated_data.pop("visible_to_users", None)

        post_list = Post_list.objects.create(**validated_data)

        if hashtags_data:
            hashtags = [Hashtag.objects.create(**item) for item in hashtags_data]
            post_list.hashtags.set(hashtags)

        if visible_to_users_data:
            post_list.visible_to_users.set(visible_to_users_data)

        return post_list
    def update(self, instance, validated_data):
        # Обновление основных полей
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.video = validated_data.get('video', instance.video)
        instance.post = validated_data.get('post', instance.post)
        instance.visible_to_users_since = validated_data.get('visible_to_users_since', instance.visible_to_users_since)

        # Обновление вложенных полей (hashtags)
        hashtags_data = validated_data.get('hashtags')
        if hashtags_data:
            hashtags = [Hashtag.objects.create(**item) for item in hashtags_data]
            instance.hashtags.set(hashtags)

        # Обновление множественного поля visible_to_users
        visible_to_users_data = validated_data.get('visible_to_users')
        if visible_to_users_data:
            instance.visible_to_users.set(visible_to_users_data)

        instance.save()
        return instance

class ModuleSerializer(serializers.ModelSerializer):
    post_list = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = ["id", "title", "images","post_list"]

    @extend_schema_field(str)
    def get_post_list(self, obj):
        post_list = obj.post_list.all() if obj.post_list else []
        return [post.title for post in post_list]

    def get_id(self, obj):
        return obj.id