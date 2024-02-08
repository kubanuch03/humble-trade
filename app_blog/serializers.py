from rest_framework import serializers
from .models import Post, Post_list, Module, Hashtag
from drf_spectacular.utils import extend_schema_field

#========= Post ================================================================
class PostSerializer(serializers.ModelSerializer):
    date_created = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Post
        fields = ["id","title", "content","date_created"]


#========= Hashtag ================================================================


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ["name","id"]

#========= Post List ================================================================
class PostListSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Post_list
        fields = [
            "id",
            "title",
            "description",
            "video",
            "post",
            "hashtags",
            "user"
            
        ]

    @extend_schema_field(str)
    def get_post_title(self, obj):
        return obj.post.title if obj.post else None

    def create(self, validated_data):
        hashtags_data = validated_data.pop("hashtags", None)
        user_data = validated_data.pop("user", None)

        post_list = Post_list.objects.create(**validated_data)

        if hashtags_data:
            post_list.hashtags.set(hashtags_data)

        if user_data:
            post_list.user.set(user_data)
       
       

        return post_list
    
    def update(self, instance, validated_data):
        hashtags_data = validated_data.get("hashtags")
        users_data = validated_data.pop("user", None)

        # instance.title = validated_data.get('title', instance.title)
        # instance.description = validated_data.get('description', instance.description)
        # instance.video = validated_data.get('video', instance.video)
        # instance.post = validated_data.get('post', instance.post)

        if users_data:
            instance.user.set(users_data)

        if hashtags_data:
            instance.hashtags.set(hashtags_data)

     
  

        instance.save()
        return instance
    




#========= Module ================================================================

class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = ["id", "title", "images","post_list"]

    

    