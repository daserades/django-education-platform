from .forms import LoginForm, RegisterForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
# Create your views here.
from django.contrib import messages

def user_register(request):
    
    if request.method == 'POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account has been created, You can Login')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'accounts/register.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form =LoginForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password= form.cleaned_data['password']
            user = authenticate(request,username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('index')
                else:
                    messages.info(request,'Disabled Account')
            else:
                messages.info(request,'Check your username and password')

    else:
        form = LoginForm()

    return render(request,'accounts/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('index')

def user_dashboard(request):
    return render()