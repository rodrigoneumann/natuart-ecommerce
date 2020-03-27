from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    messages.sucess(request, "You have successfully been logged off")
    return redirect(reverse("index"))
