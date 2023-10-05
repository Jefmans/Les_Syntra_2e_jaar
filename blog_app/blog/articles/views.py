from django.shortcuts import render, get_object_or_404
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
    pass

def author_create(request):
    pass

def articles_per_author_list(request):
    pass