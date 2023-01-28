from django.db import models

# Create your models here.
class bookdb(models.Model):
    Name=models.CharField(max_length=50,blank=True,null=True)
    Aname=models.CharField(max_length=50,blank=True,null=True)
    Price=models.IntegerField(blank=True,null=True)
    Image=models.ImageField(upload_to='Profile',null=True,blank=True)

class categorydb(models.Model):
    Category=models.CharField(max_length=50,blank=True,null=True)
    # Description=models.CharField(max_length=100,blank=True,null=True)
    Image=models.ImageField(upload_to='Profile',null=True,blank=True)

class productdb(models.Model):
    Product=(models.CharField(max_length=50,null=True,blank=True))
    # Description=(models.CharField(max_length=50,null=True,blank=True))
    Image=models.ImageField(upload_to='Profile',null=True,blank=True)
    PCategory=models.CharField(max_length=50,blank=True,null=True)
    PPrice=models.IntegerField(blank=True,null=True)
    
class frontregisterdb(models.Model):
    Username = (models.CharField(max_length=50, null=True, blank=True))
    Email = (models.CharField(max_length=50,null=True,blank=True))
    Image = models.ImageField(upload_to='Profile', null=True, blank=True)
    Password = models.CharField(max_length=50, blank=True, null=True)
    Cpassword = models.CharField(max_length=50,blank=True, null=True)





