from django.contrib import admin
from .models import Product,Variation
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    search_fields=('product_name','price','stock','category','created_date')
    prepopulated_fields= { 'slug' : ('product_name',)}
    list_display= ('product_name','price','stock','category','created_date','is_avilable')

class VariationAdmin(admin.ModelAdmin):
    list_display= ('product','variation_category','variation_value','is_active')
    list_editable=('is_active',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,VariationAdmin)