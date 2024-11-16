from django.contrib import admin
from users.models import Profile, Ticket, CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ["email", "is_superuser", "is_active", "created_at"]
    list_filter = ["email", "is_superuser", "is_active"]
    search_fields = ["email"]
    ordering = ["created_at"]
    fieldsets = (
        ("Authentication", {
            "fields": (
                'email', 'password',
            ),
        }),
        ("Permissions", {
            "fields": (
                "is_staff", "is_superuser", "is_active",
            ),
        }),
        ("Group Permissions", {
            "fields": (
                "groups", "user_permissions",
            ),
        }),
        ("Dates", {
            "fields": (
                "last_login",
            ),
        }),
    )
    add_fieldsets = (
        ("Add User", {
            "fields": (
                "email", "password1", "password2", "is_staff", "is_active", "is_superuser",
            )
        }),
    )


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user"]
    search_fields = ["user"]


class TicketAdmin(admin.ModelAdmin):
    list_display = ["author", "subject", "created_date", "updated_date"]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Ticket, TicketAdmin)
