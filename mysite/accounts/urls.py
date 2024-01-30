from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('sign_up/', views.sign_up_view, name="sign_up"),
    path("sign_in/", views.login_view, name="sign_in"),
    path("logout/", views.logout_view, name="logout")
]
