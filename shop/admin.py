from django.contrib import admin
from shop.models.category import Category
from shop.models.customer import Customer
from shop.models.image import Image
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display= ('name',)
   
admin.site.register(Category,CategoryAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','phone','email','password')

admin.site.register(Customer,CustomerAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display=('name','image_file','price','description','photographer','created_at','updated_at')

admin.site.register(Image,ImageAdmin)

