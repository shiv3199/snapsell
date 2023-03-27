from django.db import models

# Create your models here.
class contactEnquiry(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=60)
    mobile=models.CharField(max_length=13)
    message=models.TextField()