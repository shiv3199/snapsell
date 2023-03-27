from django.contrib import admin
from home.models import contactEnquiry
class contactEnquiryAdmin(admin.ModelAdmin):
    list_display=('name','email','mobile','message')


admin.site.register(contactEnquiry,contactEnquiryAdmin)

# Register your models here.
