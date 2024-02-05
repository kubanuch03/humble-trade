from django.contrib import admin

from app_clients.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "phone_number",
        "created_at",
    )
    search_fields = ("username", "email", "phone_number", "created_at")
    list_filter = ("is_staff", "created_at")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "username",
                    "full_name",
                    "phone_number",
                    "bio",
                    "avatar",
                )
            },
        ),
        (
            "Location",
            {
                "fields": (
                    "location",
                    "address",
                    "address_line2",
                    "city",
                    "state",
                    "country",
                    "zip",
                    "tax_id",
                )
            },
        ),
        ("Social Media", {"fields": ("facebook", "instogram", "twitter")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_client", "is_active", "created_at")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "full_name",
                    "phone_number",
                ),
            },
        ),
    )
    readonly_fields = ("created_at",)


admin.site.register(Client, ClientAdmin)
