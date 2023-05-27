from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.forms import Textarea
from django.db import models

@admin.register(CustomUser)
class UserAdminConfig(UserAdmin):
    ordering = ('-create_dt',)
    list_display = ('user_id', 'username', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        ('Personal', {'fields': ('email', 'phone', 'profile_img',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Dates', {'fields': ('create_dt', 'update_dt'), 'classes': ('collapse',)}),
    )

    readonly_fields = ('create_dt', 'update_dt')

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('username', 'password', 'is_active', 'is_staff')}
        ),
    )