from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Genre

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'is_bot_flag',
                ),
            },
        ),
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre_name']
    search_fields = ['genre_name']


