from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import *
from .models import Dashboard


def register_user(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            Dashboard.objects.create(user=user)
            return render(request, "registration/register_done.html", {"user": user})
    else:
        form = UserRegister()
        return render(request, "registration/register.html", {"form": form})



def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully !!!")
            return redirect("home")
        else:
            messages.success(request, "There was an error logging in , try again....")
            return redirect("login")
    return render(request, "registration/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out !!!")
    return redirect("home")


def dashboard(request):
    user = request.user
    return render(request, "registration/profile.html", {"user": user})
