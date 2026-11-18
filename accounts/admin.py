
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_staff",
    )

    list_filter = (
        "role",
        "is_staff",
        "is_active",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "InSureRance Profile",
            {
                "fields": (
                    "role",
                    "contact_number",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "InSureRance Profile",
            {
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "role",
                    "contact_number",
                )
            },
        ),
    )
