from django.contrib import admin
from .models import Post, Post_list, Module, Hashtag


class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1


class PostListAdmin(admin.ModelAdmin):
    inlines = [ModuleInline]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date_created")
    prepopulated_fields = {"slug": ("title",)}  # автоматически заполнять slug из title
    search_fields = ("title", "content")  # добавление поля поиска


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Post_list, PostListAdmin)
