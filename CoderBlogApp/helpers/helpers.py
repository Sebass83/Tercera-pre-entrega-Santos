from CoderBlogApp.models import *
from django.shortcuts import render

def helperPostRequest(request, termino):
    if termino.startswith("@"):
        termino = termino.replace("@", "")
        print({"termino": termino})
        try:
            data = EntryBlogData.objects.get(slug=termino)
            print({"slug": data.slug, "author": data.author})
        except Exception as e:
            if type(e).__name__ == "DoesNotExist":
                return render(
                    request,
                    "post.html",
                    {"error": f'No se encontró el post con el Slug "{data}"'},
                )
        summary = BlogSummary.objects.get(id=data.id)
        blog = Blog.objects.get(id=data.id)

        return render(
            request, "post.html", {"summary": summary, "blog": blog, "data": data}
        )
    termino = request.GET["termino"]
    try:
        summary = BlogSummary.objects.get(title=termino)

    except Exception as e:
        if type(e).__name__ == "DoesNotExist":
            return render(
                request,
                "post.html",
                {"error": f'No se encontró el post con el Titulo "{termino}"'},
            )

    blog = Blog.objects.get(id=summary.id)
    data = EntryBlogData.objects.get(id=summary.id)

    return render(
        request, "post.html", {"summary": summary, "blog": blog, "data": data}
    )



def helperNewPost(request):
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
            hero_img_url=hero_img_url,
        )
        EntryBlogData.objects.create(author=author, slug=slug)


def helperGetAllPosts(request):
    cards = BlogSummary.objects.all()
    data = EntryBlogData.objects.all()
    return render(request, "inicio.html", {"cards": cards, "data": data})

