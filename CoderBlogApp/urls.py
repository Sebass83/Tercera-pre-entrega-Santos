from django.urls import path
from CoderBlogApp.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("crear_post/", crear_post, name="crear_post"),
    path("post/", post, name="post"),
]
