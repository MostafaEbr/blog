from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import forms


# Create your views here.


def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, "articles/index.html", {
        "articles": articles
    })


@login_required(login_url='/accounts/sign_in/')
def articles_details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, "articles/article_details.html", {
        "article": article
    })


@login_required(login_url='/accounts/sign_in/')
def add_articles(request):
    if request.method == "POST":
        form = forms.CreateArticles(request.POST, request.FILES)
        if form.is_valid():
            # todo Save form Articles
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("articles:index")
    else:
        form = forms.CreateArticles()
    return render(request, "articles/add_articles.html", context={
        "form": form
    })
