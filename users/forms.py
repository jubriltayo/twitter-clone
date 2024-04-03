from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=25, required=False)
    last_name = forms.CharField(max_length=25, required=False)
    bio = forms.CharField(max_length=100, required=False)
    
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'image', 'bio']
    
