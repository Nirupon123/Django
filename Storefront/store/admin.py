from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','inventory','unit_price','inventory_status']
    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory <60 and product.inventory>30:
            return "Medium"
        if product.inventory < 20:
            return "Low"
        return "High"

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display=['title','featured_product']

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','membership']
    list_editable=['membership']
    list_display_links = ['email']
