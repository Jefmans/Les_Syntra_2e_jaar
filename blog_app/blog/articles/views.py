from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Author

# Create your views here.

def article_list(request):
    articles_all = Article.objects.all()
    template = "articles/article_list.html"
    context = {
        "articles" : articles_all
    }
    return render(request=request, template_name=template, context=context)


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    template = "articles/article_detail.html"
    context = {
        "article" : article
    }
    return render(request=request, template_name=template, context=context)


def author_list(request):
    author_list = Author.objects.all()
    template = "articles/author_list.html"
    context = {
        "authors" :  author_list,
    }
    return render(request=request, template_name=template, context=context)

def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    template = "articles/author_detail.html"
    context = {
        "author" :  author,
    }
    return render(request=request, template_name=template, context=context)


def article_create(request):
    print(request.body)
    print(request.POST)
    template = "articles/article_create.html"
    
    if request.method == "POST":
        print(request.POST['author'])
        if request.POST['title'] and request.POST['short_description'] and request.POST['description'] and request.POST['author']:
            try:
                print('---------1---------------')
                author = get_object_or_404(Author, pk = request.POST['author'])
                print('---------2---------------')
                article = Article(title=request.POST['title'], short_description= request.POST
                ['short_description'], description = request.POST['description'], author =author)
                print('---------3---------------')
                article.save()
                print('---------4---------------')
                return redirect("articles:article_list")
            except:
                pass
    authors = Author.objects.all()
    context = {
        "authors" : authors,
    }
    return render(request=request, template_name=template, context=context)


def author_create(request):
    pass

def articles_per_author_list(request):
    pass