from django.contrib import admin
from .models import *


@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "image","title", "url", "category")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "image")


