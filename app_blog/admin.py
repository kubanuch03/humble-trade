from django.contrib import admin
from .models import Post, Post_list, Module, Hashtag


# class ModuleInline(admin.StackedInline):
#     model = Module
#     extra = 1

@admin.register(Post_list)
class PostListAdmin(admin.ModelAdmin):
    list_display = ["title","post","id",]
    # inlines = [ModuleInline]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id","title", "date_created")
    # prepopulated_fields = {"slug": ("title",)}  # автоматически заполнять slug из title
    search_fields = ("title", "content")  # добавление поля поиска


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ["name","id"]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ["title","id","post_list",]
