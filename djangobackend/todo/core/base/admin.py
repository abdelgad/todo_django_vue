from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Todo
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ("myusername",)

    def myusername(self, obj):
        url = (
            reverse("admin:todobase_todo_changelist")
            + "?"
            + urlencode({"owner__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{}</a>', url, obj.username)

    myusername.short_description = "username"


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):

    actions = ['make_checked']

    def make_checked(self, request, queryset):
        queryset.update(checked=True)

    make_checked.short_description = "Check selected todos"
