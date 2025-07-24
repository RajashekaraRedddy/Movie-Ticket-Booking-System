from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','phone', 'password1', 'password2','is_theater_manager'] 

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder':'enter username'}),
            'password' : forms.PasswordInput(attrs={'placeholder' : 'enter password'})
        } 