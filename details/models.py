from __future__ import unicode_literals

from django.db import models

# Create your models here.

#e.g motel
class Category(models.Model):
    Name= models.CharField(max_length=30)

    def __str__(self):
        return self.Name

class Place_details(models.Model):
    Name = models.CharField(max_length = 30)
    Location = models.CharField(max_length=30)
    Price = models.DecimalField(max_digits=100,decimal_places=2)
    Category = models.ForeignKey(Category)
    Pics = models.ImageField(blank=True)#(upload_to='media')
    
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    slug = models.SlugField(max_length=255, unique=True)
   
    def __str__(self):
        return self.Name

class Home_page_pic(models.Model):
      Hpic=models.ImageField(blank=True)
      Dis= models.TextField()
      _active=models.CharField(max_length= 30)




    
    
