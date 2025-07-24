from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .utils import get_otp
from django.http import HttpResponse
from django.contrib.auth.forms import UserChangeForm,AuthenticationForm,PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail 
from django.contrib import messages 
from django.contrib.auth.models import User 
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerview(request):
    fm=RegistrationForm() 
    context={'form':fm}
    if request.method=='POST':
        user=RegistrationForm(request.POST)
        if user.is_valid():
            user.save()
            username = user.cleaned_data['username']
            email = user.cleaned_data['email']
            send_mail(
                'Registration Successful',                                                             
                f'{username} You have successfully logged in to our site.\n\nYour email: {email}',               
                'rajashekara831@gmail.com',        
                [email],  
                fail_silently=True  
            ) 
            return HttpResponse('user created successfully')
    return render(request, 'account/register.html', context)     

@login_required(login_url='signin/') 
def Loginview(request):
    context={
        'form' : LoginForm()  
    }
    if request.method=='POST':
        fm = LoginForm(data=request.POST) 
        if fm.is_valid():
            
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(request,username=username, password=password)
            if user is not None:
                if user.is_authenticated:
                    login(request,user) 
                    messages.success(request,'Login Successful') 
                    
                    email = user.email  
                
                    if email:
                        send_mail(
                            'Login Successful',                                                             
                            f'You have successfully logged in to our site.\n\nYour email: {email}',               
                            'rajashekara831@gmail.com',        
                            [email],  
                            fail_silently=True  
                        ) 
                    messages.success(request,'Login Successful') 
                    return redirect('home')
        return HttpResponse('Invalid Username or Password') 
    return render(request,'account/login.html',context) 

def logoutView(request):
    logout(request)
    messages.error(request,'Logout Successful') 
    return redirect('signin')

# def identify_view(request):
#     fm = IdentifyUser(data=request.POST) 
#     if request.method == 'POST':
#         if fm.is_valid():
#             username = fm.cleaned_data['username'] 
#             user = User.objects.get(username = username)
#             return redirect(f'/reset_pwd/{user.username}/') 
#             # return redirect(reverse('reset_password', kwargs={'username': user.username})) 
#     return render(request, 'identify.html',context={'form' : fm}) 


@login_required(login_url='signin/') 
def home(request):
    return render(request, 'account/home.html') 