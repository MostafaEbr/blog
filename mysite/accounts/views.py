from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def sign_up_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Login User to system
            return redirect("articles:index")
    else:
        form = UserCreationForm()
    return render(request, "accounts/sign_up.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Login User to system
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("articles:index")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/sign_in.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("articles:index")
