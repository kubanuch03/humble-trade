from django import forms
from .models import Hashtag, Post, Post_list, Module


class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ["name", "id"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "slug", "content", "images"]


class PostListForm(forms.ModelForm):
    class Meta:
        model = Post_list
        fields = ["post", "title", "description", "picter", "video", "hashtags"]


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ["post_list", "title", "description", "images"]