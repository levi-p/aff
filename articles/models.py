from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

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

    def __str__(self):
        return self.Title
    
    def get_absolute_url(self):
        return reverse('art:article',kwargs={'article_id':self.id,})
    


    

    
