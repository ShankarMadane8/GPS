from math import frexp
import re
from django.shortcuts import render
from .forms import RegisterForm
from .models import Register,Images
# Create your views here.


def register(request):
  msg=""
  if request.method=="POST":
    forms=RegisterForm(request.POST)
    if forms.is_valid():
      forms.save()
      msg="Congratulations, your account has been successfully created"
  else:  
    forms=RegisterForm() 
  return render(request,"app/register.html",{"forms":forms,"msg":msg})






  
def login(request):
  if request.method=="POST":    
    email=request.POST['email']
    password=request.POST['password']
    errors=None
    try:
      register=Register.objects.get(email=email)
    except:
      errors='Enter valid email and password !!!'
      
    if not errors:
      if password==register.password:
        request.session["users"]=register.first_name
        return render(request,'app/dashboard.html',{"users":request.session.get("users")})
      else:
        errors='Enter valid  password !!!'
    
    fm=RegisterForm()
    return render(request,'app/login.html',{"forms":fm,"errors":errors})

  else:
    fm=RegisterForm()
    return render(request,'app/login.html',{"forms":fm})

  