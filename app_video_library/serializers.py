from rest_framework import serializers
from .models import *
from drf_spectacular.utils import extend_schema
from typing import Optional

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class VideoCourseSerializer(serializers.ModelSerializer):
    category_title = serializers.SerializerMethodField()

    @extend_schema(str)
    def get_category_title(self, obj)-> Optional[str]:
        return obj.category.title if obj.category else None

    class Meta:
        model = Courses
        fields = ["id","category", "category_title", "title", "image", "url"]