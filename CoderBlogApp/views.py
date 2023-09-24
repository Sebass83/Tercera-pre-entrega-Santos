from django.shortcuts import render
from CoderBlogApp.helpers.helpers import *

# Create your views here.


def inicio(request):
    return getAllPosts(request)


def crear_post(request):
    helperNewPost(request)
    return render(request, "crear_post.html")


def post(request):
    if request.GET["termino"]:
        termino = request.GET["termino"]
        return helperPostRequest(request, termino)
    return render(request, "inicio.html")
