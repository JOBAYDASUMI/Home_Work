from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from django.db import IntegrityError
from django.db.models import Q

from django.contrib import messages


# This is authencation part start

def homePage(req):
    
    return render(req,'common/homePage.html')

def logoutPage(req):
    logout(req)
    messages.warning(req,"You Are Successfully Logout Please Login")
    return redirect("loginPage")

def loginPage(req):
    if req.method == 'POST':
        Username=req.POST.get('username')
        Usertype=req.POST.get('password')
        
        if not Username or not Usertype:
            messages.warning(req, "Both Username and password are required")
            return render(req, "loginPage.html")

        user = authenticate(username=Username, password=Usertype)

        if user is not None:
            login(req, user)
            messages.success(req, "Login Successfully")
            return redirect("JobFeedPage")
        else:
            messages.warning(req, "Invalid username or password")
    
    return render(req,'common/loginPage.html')

def registerPage(req):
    if req.method == 'POST':
        Username=req.POST.get('username')
        Usertype=req.POST.get('usertype')
        Email=req.POST.get('email')
        Password=req.POST.get('password')
        Confirmpassword=req.POST.get('confirmpassword')
        
        if not all([Username,Usertype,Email,Password,Confirmpassword]):
            messages.warning(req, "All Feild Are quired")
            return render(req,"common/registerPage.html")
        try:
            validate_email(Email)
        except ValidationError:
            messages.warning(req,"Invalid Email Formate")
            return render(req,"common/registerPage.html")
        if Password != Confirmpassword:
            messages.warning(req,"Password Not Match")
            return render(req,"common/registerPage.html")
        if len(Password) < 8:
            messages.warning(req,"password Must be at leaste 8 charecter long")
            return render(req,"common/registerPage.html")
        if not any(char.isdigit() for char in Password) or not any(char.isalpha() for char in Password):
            messages.warning(req, "Password must contain both letters and numbers")
            return render(req, "common/registerPage.html")
        try:
            user=CustomUser.objects.create_user(
                username=Username,
                user_type=Usertype,
                email=Email,
                password=Password,
            )
            messages.success(req, "Account created successfully! Please log in.")
            return redirect("loginPage")
        except IntegrityError:
            messages.warning(req, "Username or email already exists")
            return render(req, "common/registerPage.html")
    
    return render(req,'common/registerPage.html')

# This is authencation part end

def JobFeedPage(req):
    
    return render(req,'myAdmin/JobFeedPage.html')