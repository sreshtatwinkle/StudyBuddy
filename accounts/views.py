from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .models import User
from django.contrib import messages



# Create your views here.
def register_form(request):
    if request.method == 'POST':
        user = User()
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.subject = request.POST['subject']
        user.subject2 = request.POST['subject2']
        user.password = request.POST['password']
        user.password2 = request.POST['password2']
        if (user.password == user.password2):
            if User.objects.filter(username=user.username).exists():
                messages.info(request,'User name already exists')
                return redirect('register')
            elif User.objects.filter(email=user.email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user.save();
                messages.info(request,'User Successfully created')
                return redirect('login')
        else:
             messages.info(request,'Password not matching')
             return redirect('register')
        return redirect('/')
    else:
       return render(request,'register.html')
        # if user.password != user.password2:
        #     return redirect('register')
        # elif user.username=='' or user.password=='':
        #     messages.info(request,'some fields are empty')
        #     return redirect('register')
        # else:
        #     user.save()
    
def login_form(request):
     if request.method == 'POST':
       user=User()
       user.username = request.POST['username']
       user.password = request.POST['password']
       user = auth.authenticate(username=user.username,password=user.password)
       if user is not None:
           auth.login(request,user)
           return redirect('/')
       else:
           messages.info(request,'Invalid Credentials')
           return redirect('login')
     else:
        return render(request,'login.html')
     
def logout(request):
    auth.logout(request)
    return redirect('/')
     
    
