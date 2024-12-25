from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm,Signupform
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,pasword=password)
            if user is not None:
                login(request,user)
                return redirect(request,'root:home')
            else:
                messages.add_message(request,messages.ERROR,'invalid')
                return render(request,'registrations/login.html')
    else:
        return render(request,'registrations/login.html')



def signup_user(request):
    if request.POST == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(request,'root:home')
        else:
            messages.add_message(request,messages.ERROR,'invalid')
            return redirect(request,'accounts:signup')
    else:
        return render(request,'registrations/signup.html')



@login_required
def logout_user(request):
    logout(request)
    return redirect(request,'root:home')

def reset_pasword(request):
    pass

def reset_pasword_done(request):
    pass

def reset_pasword_coniform(request):
    pass

def reset_pasword_complate(request):
    pass

def edit_profile(request):
    pass
