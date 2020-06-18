from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm, UserChangeProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'You Logged in successfully', 'success')
                return redirect('shop:home')
            else:
                messages.error(request, 'username or password is wrong', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/user_login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You Logged out successfully', 'success')
    return redirect('shop:home')


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['full_name'], cd['password2'])
            user.save()
            messages.success(request, 'You Registered successfully', 'success')
            return redirect('shop:home')

    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/user_register.html', {'form': form})


@login_required
def profile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = UserChangeProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile successfully changed', 'success')
            return redirect('accounts:profile')
    else:
        form = UserChangeProfileForm(instance=user)
    return render(request, 'accounts/profile.html', {'user': user, 'form': form})
