from django.contrib import admin

from .models import User


def deactivate_users(modeladmin, request, queryset):
    queryset.update(is_active=False)


def activate_users(modeladmin, request, queryset):
    queryset.update(is_active=True)


deactivate_users.short_description = "Deactivate users"
activate_users.short_description = "Activate users"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'last_login',
        'date_joined',
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (
        'is_staff', 'is_active', 'last_login', 'date_joined'
    )
    ordering = (
        'username', 'first_name', 'last_name', 'last_login', 'date_joined'
    )
    actions = [deactivate_users, activate_users]
