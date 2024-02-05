from django.contrib import admin
from app_resourse_center.models import Category, Document


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "image")


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        "image",
        "title",
        "post",
        "url",
        "id",
    )
