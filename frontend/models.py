from django.db import models

# Create your models here.
class frontregisterdb(models.Model):
    Username = (models.CharField(max_length=50, null=True, blank=True))
    Email = (models.CharField(max_length=50,null=True,blank=True))
    Password = models.CharField(max_length=50, blank=True, null=True)
    Cpassword = models.CharField(max_length=50,blank=True, null=True)

