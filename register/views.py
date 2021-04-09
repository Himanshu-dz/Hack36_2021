from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):
      if request.method=='POST':
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            username=request.POST['email']
            email=request.POST['email']
            pwd=request.POST['password1']
            cnfrm_pwd=request.POST['password2']

            if pwd==cnfrm_pwd:
                  if User.objects.filter(username=username).exists():
                        print('username taken')
                  elif User.objects.filter(email=email).exists():
                        print('email exists already')
                  else:
                         user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=pwd)
                         user.save()

            else:
                  print("password didn't matched")             
            return redirect('/')     





                
      else:      
             return render(request,'register.html')