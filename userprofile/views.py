from django.shortcuts import render, redirect
from .form import RegUserForm,Reg_UserProfile_Form,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import User_Profile




def registration(request):
   if request.method =='POST':
       username = request.POST.get('username')
       email = request.POST.get('email')
       password = request.POST.get('password')
       password2 = request.POST.get('password2')
       if (password == password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save();
                messages.info(request,'User Successfully created')
                return redirect('login')
       else:
             messages.info(request,'Password not matching')
             return redirect('register')
       return redirect('/')
   else:
       return render(request,'register.html')




def login_form(request):
     if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       print(username,password)
       user = authenticate(request,username=username,password=password)
       if user is not None:
           login(request,user)
           return redirect('addmodules')
       else:
           messages.info(request,'username or password not correct!!')
     return render(request,'login.html')
    #    

     
def logout_form(request):
    logout(request)
    return redirect('/') 




# def addmodules(request):
#     if request.method == 'POST':
#         form = Reg_UserProfile_Form(request.POST, request.FILES)
#         if form.is_valid():
#             user_profile = form.save(commit=False)
#             user_profile.user = request.user  # Assuming the user is logged in
#             user_profile.save()
#             return redirect('/')
#             # You can add any additional logic or messages here
#     else:
#         form = Reg_UserProfile_Form()
    
#     context = {
#         'form': form
#     }
    
#     return render(request, 'reg_module.html', context)


from .models import User_Profile

def addmodules(request):
    # Assuming the user is logged in
    user_profile = User_Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = Reg_UserProfile_Form(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            # Redirect or provide a success message
            return redirect('/')
    else:
        form = Reg_UserProfile_Form(instance=user_profile)

    context = {
        'form': form
    }

    return render(request, 'reg_module.html', context)


def profiles(request):
    user_profiles = User_Profile.objects.all()
    context = {
        'user_profiles': user_profiles
    }

    return render(request, 'profiles.html', context)
