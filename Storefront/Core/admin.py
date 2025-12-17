from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.contrib.contenttypes.admin import GenericTabularInline
from tags.models import tagedItem

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, { 
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2','first_name','last_name'),
        }),
    )

class TagInline(GenericTabularInline):
    autocomplete_fields=['tag']
    model=tagedItem
    
