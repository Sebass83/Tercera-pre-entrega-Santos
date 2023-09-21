from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.


def inicio(request):
    cards = BlogSummary.objects.all()



    return render(request, "inicio.html", {"cards": cards})


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


        
def post(request):
    if request.GET['termino']:
        termino = request.GET['termino']
        print(termino)

        try:
            
            summary = BlogSummary.objects.get(title=termino)
            
        except Exception as e:
            if type(e).__name__ == 'DoesNotExist':
                return render(request, "post.html",{'error': f'No se encontro el post con el Titulo \"{termino}\"'})
        
        if summary:
                print(summary.id)
                return render(request, "post.html")

        


        summary = BlogSummary.objects.get(title=termino)
        if summary:
            print(summary.id)
            return render(request, "post.html")
       
    return render(request, "inicio.html")

