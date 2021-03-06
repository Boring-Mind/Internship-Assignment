from datetime import datetime as dt

import pytz
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path

from .models import User


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
        'since_last_login',
        'date_joined',
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (
        'is_staff', 'is_active', 'last_login', 'date_joined'
    )
    ordering = (
        'username',
        'first_name',
        'last_name',
        'last_login',
        'date_joined',
    )
    change_list_template = "admin_user_actions.html"

    def get_new_users_count(self) -> int:
        return User.objects.filter(
            date_joined__gt=dt.now(pytz.utc).date()
        ).count()

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['registered_last_day'] = self.get_new_users_count()
        return super(UserAdmin, self).changelist_view(
            request, extra_context=extra_context
        )

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('activate_users/', self.activate_users),
            path('deactivate_users/', self.deactivate_users),
        ]
        return my_urls + urls

    def activate_users(self, request):
        self_id = request.user.id
        self.model.objects.exclude(id=self_id).update(is_active=True)
        self.message_user(request, "All users are activated")
        return HttpResponseRedirect("../")

    def deactivate_users(self, request):
        self_id = request.user.id
        self.model.objects.exclude(id=self_id).update(is_active=False)
        self.message_user(request, "All users are deactivated")
        return HttpResponseRedirect("../")
