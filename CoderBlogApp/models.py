from django.db import models

# Create your models here.

class blogSummary(models.Model):
    titles = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    entryDate = models.DateField(auto_now_add=True)
    min_img_url= models.URLField()


class blog(models.Model):
    post = models.CharField(max_length=200)
    hero_img_url = models.URLField
    quote = models.CharField(max_length=30)
    acent_img_url= models.URLField()

class entryBlog(models.Model):
    author = models.CharField(max_length=200)
    entryDate = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=200, unique=True)
    
