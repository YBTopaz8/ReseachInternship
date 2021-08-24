from math import trunc
from django.db import models
from django.db.models.fields.related import OneToOneField

from django_resized import ResizedImageField

from django.urls import reverse

from django.contrib.auth.models import User

from django.templatetags.static import static

import random

# Create your models here.

class Categories(models.Model):
    name = models.CharField( max_length=50)
    
    def __str__(self):
        return self.name
    def get_url(self):
            return reverse('edit_cat', args=[self.name])

class Articles(models.Model):
    art_publisher=models.ForeignKey(User, on_delete=models.CASCADE, default="")
    art_title= models.CharField( max_length=250)
    art_code=models.CharField( max_length=7, default="A"+''.join(random.choice('1234567890') for i in range(6)))
    art_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    art_volume = models.IntegerField(default=1)
    art_date = models.DateField( auto_now=True)
    art_created_date = models.DateField( auto_now_add=True)
    art_description= models.CharField(max_length=50, default="", blank=True)
    art_cover = ResizedImageField( size=[570, 480], quality=80, upload_to='uploads/article_cover/',  blank=True, null=True)
    art_document = models.FileField( upload_to='uploads/article_document/', null=True, blank=True)
    
    def __str__(self):
        return f'({self.art_code}) {self.art_title} BY {self.art_publisher.username}'
        #return self.art_title
    
    @property
    def get_category(self):
        return self.art_category.name 
    
    def get_art_cover(self):
        if self.art_cover:
            return self.art_cover.url
        else:
            return static("images/article_205px.png")
    
    def get_art_document(self):
        if self.art_document:
            return self.art_document.url
        else:
            return None

    """
    code
    category
    publisher
    volume
    date
    cover
    doc
    """