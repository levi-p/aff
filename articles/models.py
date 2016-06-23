from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Comments(models.Model):
    Name = models.CharField(max_length=30,default='anonymous')
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.Name


class Article_details(models.Model):
    Title = models.CharField(max_length=30)
    Article = models.TextField()
    Pic = models.ImageField(blank=True)
    Comments = models.ForeignKey(Comments,default='one')
    


    

    
