from django.urls import path
from . import views


app_name = "articles"
urlpatterns = [
    path('', views.articles_list, name="index"),
    path("create", views.add_articles, name="create"),
    path("<str:slug>", views.articles_details, name="details"),
]

