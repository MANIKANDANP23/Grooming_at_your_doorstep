from django.shortcuts import render,redirect
from prakash_project import settings
from shop.form import CustomUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import json
from django.http import JsonResponse
from django.core.mail import EmailMessage,send_mail
# Create your views here.
def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,"shop/home.html",{"products":products})

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"logged in successfully")
                 #EMAIL
                subject ="Welcome to Django-Login!!"
                message = f"Hello {user.username}!! \nWelcome to the Homies \nThanking You for Login"
                from_email= settings.EMAIL_HOST_USER
                to_list= [user.email]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
                return redirect("/")
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect("/login")
        return render(request,"shop/login.html")    

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect("/")

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request,"Registration Success You can Login Now..!")
            subject ="Welcome to Django-Login!!"
            message = f"Hello {user.username}!! \nWelcome to the Homies \nThanking You for Creating your profile"
            from_email= settings.EMAIL_HOST_USER
            to_list= [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            return redirect('/login')
    return render(request,"shop/register.html",{"form":form})

def collections(request):
    catagory = Catagory.objects.filter(status=0)
    return render(request,"shop/collections.html",{"catagory":catagory})

def service(request,id):
    product = Product.objects.filter(shop_name_id=id)
    return render(request,"shop/products/service.html",{"data":product})

    

def service_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/service_details.html",{"products":products})
        else:
            messages.error(request,"No Such Catagory Found")
            return redirect('collections')
    else:
        messages.error(request,"No Such Catagory Found")
        return redirect('collections')
    
def shop_name(request,id):
    shop = shopname.objects.filter(catagory_id=id)
    return render(request,"shop/products/shopname.html",{'shop':shop}) 

def aboutus(request):
    return render (request,'aboutus.html')   

def support(request):
    return render (request,'support.html')    

def privacypolicy(request):
    return render (request,'privacypolicy.html')    

def termsofuse(request):
    return render (request,'termsofuse.html')   
   