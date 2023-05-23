from django.contrib import admin
from shop.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_id','product_name','category','subcategory','price','desc','pub_date','image')
admin.site.register(Product,ProductAdmin)
