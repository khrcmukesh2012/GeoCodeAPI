from django.db import models

# Create your models here.
class Address(models.Model):
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=30,null=True,blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    pin_code = models.CharField(max_length=50,null=True,blank=True)
    lat = models.FloatField(null=True,blank=True)
    log = models.FloatField(null=True,blank=True)


    def __str__(self):
    	return self.address