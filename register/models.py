from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sign_up(models.Model):
    Name=models.CharField(max_length=30, default='h')
    Email=models.EmailField(blank=True,default='h')
    password=models.CharField(max_length=30,default='h')
    enter_password=models.CharField(max_length=30,default='h')
    

    
