from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

from .forms import SignUpForm, EditProfileForm
# Create your views here.

def home(request):
    return render(request, 'accounts/home.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have Successfully Logged In!'))
            return redirect('home')
            # Redirect to a success page.
        else: 
            messages.success(request, ('Error, please try again!'))
            return redirect('login')
    else:
        return render(request, 'accounts/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You Have Been Logged Out!'))

    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form  = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You Have Successfully Logged In!'))
            return redirect('home') 

    else:
        form = SignUpForm()
    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)



def edit_profile(request):
    if request.method == 'POST':
        form  = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You Have Edited Your Profile !'))
            return redirect('home') 

    else:
        form = EditProfileForm( instance=request.user)
    context = {
        'form': form
    }

    return render(request, 'accounts/edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form  = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)

            messages.success(request, ('You Have Changed Your Password !'))
            return redirect('home') 

    else:
        form = PasswordChangeForm( user=request.user)
    context = {
        'form': form
    }

    return render(request, 'accounts/change_password.html', context)
