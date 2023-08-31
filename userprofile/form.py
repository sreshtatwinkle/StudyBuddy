from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User_Profile

class RegUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class Reg_UserProfile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ('bio', 'module', 'module2', 'profile_pic')

class RegisterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_form = RegUserForm()
        self.profile_form = RegUserProfileForm()