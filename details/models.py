from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

#e.g motel
class Category(models.Model):
    Name= models.CharField(max_length=30)

    def __str__(self):
        return self.Name


class Roomz(models.Model):
    RoomName = models.CharField(max_length=30)
    Occupants = models.IntegerField(blank=True)
    Price = models.DecimalField(max_digits=100,decimal_places=2,blank=True)
    RoomPics=models.ImageField(blank=True)
    def __str__(self):
        return self.RoomName

class place_details(models.Model):
    Name = models.CharField(max_length = 30)
    Location = models.CharField(max_length=30)
    Room = models.ManyToManyField(Roomz)
    Category = models.ForeignKey(Category)
    Pics = models.ImageField(blank=True)#(upload_to='media')
    Discription=models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    slug = models.SlugField(max_length=255, unique=True)

    def get_absolute_url(self):
        return reverse("Det:Place_details",kwargs={'place_id':self.id})
   
    def __str__(self):
        return self.Name

class Home_page_pics(models.Model):
      Location= models.CharField(max_length=30, blank=True)
      Hpic=models.ImageField(blank=True)
      Dis= models.TextField(blank=True)
      _active=models.CharField(max_length= 30,blank=True)
      Name=models.CharField(max_length = 30,blank=True)
      class Meta:
        ordering = ['Name']
      
      def __str__(self):
        return self.Name

class Social_ps(Home_page_pics): 
      
      
      def __str__(self):
        return self.Name



      


