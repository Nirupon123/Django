from django.contrib import admin
from . import models
# Register your models here.
  

@admin.register(models.tag)
class tagAdmin(admin.ModelAdmin):
    search_fields=['label']