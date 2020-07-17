from __future__ import annotations

from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display = (
        "first_name",
        "last_name",
        "username",
        "date_joined",
        "is_active",
    )
    search_fields = (
        "user__first_name",
        "user__last_name",
        "user__email",
        "user__username",
    )


admin.site.register(User, UserAdmin)
