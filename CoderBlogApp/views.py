from django.shortcuts import render
from .models import *

# Create your views here.


def inicio(request):
    return render(request, "inicio.html")


def crear_post(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        author = request.POST["author"]
        min_img_url = request.POST["min_img_url"]
        post = request.POST["post"]
        hero_img_url = request.POST["hero_img_url"]
        quote = request.POST["quote"]
        acent_img_url = request.POST["acent_img_url"]
        slug = title.strip().lower().replace(" ", "-")

        BlogSummary.objects.create(
            title=title,
            description=description,
            author=author,
            min_img_url=min_img_url,
        )
        Blog.objects.create(
            post=post,
            quote=quote,
            acent_img_url=acent_img_url,
            hero_img_url=hero_img_url
        )
        EntryBlogData.objects.create(author=author, slug=slug)

    return render(request, "crear_post.html")


# class BlogSummary(models.Model):
#     titles = models.CharField(max_length=200, unique=True)
#     description = models.CharField(max_length=200)
#     author = models.CharField(max_length=200)
#     entryDate = models.DateField(auto_now_add=True)
#     min_img_url= models.URLField()


# class Blog(models.Model):
#     post = models.CharField(max_length=200)
#     hero_img_url = models.URLField
#     quote = models.CharField(max_length=30)
#     acent_img_url= models.URLField()

# class EntryBlogData(models.Model):
#     author = models.CharField(max_length=200)
#     entryDate = models.DateField(auto_now_add=True)
#     slug = models.CharField(max_length=200, unique=True)
