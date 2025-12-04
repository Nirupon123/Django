from django.contrib import admin
from . import models
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.contrib.contenttypes.admin import GenericTabularInline
from tags.models import tagedItem


# Register your models here.

class TagInline(GenericTabularInline):
    autocomplete_fields=['tag']
    model=tagedItem
    
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[TagInline]
    prepopulated_fields={
        'slug': ['title']
    }
    list_display=['title','inventory','unit_price',
                  'collection','inventory_status']
    list_editable=['unit_price','inventory']
    list_filter = ['collection','last_update']
    search_fields = ['title__istartswith']
    actions=['clear_inventory']
    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory <60 and product.inventory>30:
            return "Medium"
        if product.inventory < 20:
            return "Low"
        return "High"
    
    def clear_inventory(self,request,queryset):
        updated_count=queryset.update(inventory=0)
        self.message_user(
            request,
            f"{updated_count} products were successfully updated."
        )


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display=['title','products_count']
    @admin.display(ordering='products_count')
    def products_count(self,collection):
        url= (
            reverse('admin:store_product_changelist')
              + '?'
              + urlencode({
                  'collection__id': str(collection.id)}))
        return format_html('<a href="{}">{}</a>',url,collection.products_count)
    
    def get_queryset(self,request): 
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )
    

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','membership','order_count']
    list_editable=['membership']
    list_display_links = ['email']
    search_fields = ['first_name__istartswith']
    list_filter = ['membership','order__placed_at']


    @admin.display(ordering='order_count')
    def order_count(self, customer):
        return customer.order_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            order_count=Count('order')
        )
   
class OrderItemInline(admin.TabularInline):
    model=models.OrderItem
    autocomplete_fields=['product']
    extra=0
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields=['customer']
    inlines=[OrderItemInline]
    list_display=['id','placed_at','customer']


