from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
#
def login(request):
     if request.method =='POST':
         uname = request.POST['username']
         pwd = request.POST['password']
         user = auth.authenticate(username=uname, password=pwd)

         if user is not None:
             auth.login(request, user)
             return redirect('/')
         else:
          messages.info(request,"invalid credentials")
          return redirect('login')
     return render(request,"login.html")
#
#
def logout(request):
     auth.logout(request)
     return redirect('/')


def register(request):
    if request.method =='POST':
        uname=request.POST['username']
        fname = request.POST['first_name']
        lname=request.POST['last_name']
        em = request.POST['email']
        pwd=request.POST['password']
        cpwd = request.POST['password1']
        if pwd==cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"Username already exists")
                return redirect('register')
            elif User.objects.filter(email=em).exists():
                messages.info(request,"Email already exists")
                return redirect('register')
            else:
                user= User.objects.create_user(username=uname,password=pwd,first_name=fname,last_name=lname,email=em)
                user.save()
                return redirect('login')
                print("User Created")
        else:
            messages.info(request, "Password not matching")
            # print("Password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
