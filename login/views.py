from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
     if request.method=='POST':
           username=request.POST['username']
           pwd=request.POST['password1']

           user=auth.authenticate(username=username,password=pwd)

           if user is not None:
                auth.login(request,user)
                return redirect('/')
           else  :
                messages.info(request,'Invalid Details')
                return redirect('login')



     else:
         return render(request,'login.html')


def logout(request):
     auth.logout(request)
     return redirect('/')         
