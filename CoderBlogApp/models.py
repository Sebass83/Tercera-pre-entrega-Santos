from django.db import models

# Create your models here.

class BlogSummary(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    entryDate = models.DateField(auto_now_add=True)
    min_img_url= models.URLField(blank=True)


class Blog(models.Model):
    post = models.CharField(max_length=200)
    hero_img_url = models.URLField(blank=True)
    quote = models.CharField(max_length=30)
    acent_img_url= models.URLField(blank=True)

class EntryBlogData(models.Model):
    author = models.CharField(max_length=200)
    entryDate = models.DateField(auto_now_add=True)
    slug = models.CharField(max_length=200, unique=True)
    
