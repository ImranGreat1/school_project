from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect('post_list')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }

    return render(request, 'registration/create_user.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    if request.GET.get('next'):
                        next_ = request.GET.get('next')
                        return redirect(next_)
                    return redirect('post_list')

    else:
        form = LoginForm()

    context = {'form': form}

    return render(request, 'registration/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('post_list')


@login_required
def user_profile(request):
    return render(request, 'user/user_profile.html')
    