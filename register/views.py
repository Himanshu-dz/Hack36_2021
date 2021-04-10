from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):
      if request.method=='POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['username']
            email=request.POST['email']
            pwd=request.POST['password1']
            cnfrm_pwd=request.POST['password2']

            if pwd==cnfrm_pwd:
                  if User.objects.filter(username=username).exists():
                        messages.info(request,'username taken')
                        return redirect('register')    
                  elif User.objects.filter(email=email).exists():
                        messages.info(request,'email exists already')
                  else:
                         user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=pwd)
                         user.save()

            else:
                  messages.info(request,"password didn't matched")   
                  return redirect('register')              
            return redirect('login')     
            
            
      else:      
             return render(request,'register.html')