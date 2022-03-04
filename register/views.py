from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
# Create your views here.
def register(request):
    if request.method=='POST':
        form=signUpForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            
    return(render(request,'register/index.html'))

def login(request):
    if request.method=='POST':
        form=signInForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return(redirect('/dashboard'))
def logout(request):
    auth_logout(request)
    return(redirect('/'))