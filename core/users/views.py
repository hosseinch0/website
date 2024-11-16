from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .forms import UserCreateForm
from django.urls import reverse
# Create your views here.


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreateForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,
                                     "You Signed up successfully")
                return HttpResponseRedirect(reverse("website:home"))
            else:
                messages.add_message(request, messages.INFO,
                                     '''Something went wrong: 
                                     1_make sure of captcha input.
                                     2_make sure your password is complex and both inputs are same''')
                return HttpResponseRedirect(reverse("users:signup"))
        form = UserCreateForm()
        return render(request, "users/signup.html", {"form": form})
    else:
        return redirect("/")


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request, email=email, password=password)
            print("some shit")
            if user != None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS,
                                     "Logged in successfully")
                return HttpResponseRedirect(reverse("website:home"))
            else:
                messages.add_message(request, messages.INFO,
                                     "Logging failed Try again")
                return HttpResponseRedirect(reverse("users:login"))
        return render(request, 'users/login.html')
    else:
        return redirect("/")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.SUCCESS, "Logged out successfully")
        return HttpResponseRedirect(reverse("website:home"))
    else:
        messages.add_message(request, messages.ERROR, "Something went wrong")
        return HttpResponseRedirect(reverse("website:home"))
