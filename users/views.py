from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from .models import Player
from datetime import date


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            name = form.cleaned_data.get('name')
            surname = form.cleaned_data.get('surname')
            user = authenticate(username=username, password=password)
            login(request, user)
            user.is_active = True
            new_user = Player.objects.create(username=username, name=name, surname=surname,
                                             registration_date=date.today())
            new_user.save()
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            Username = form.data['username']
            Password = form.data['password']
            user = authenticate(request, username=Username, password=Password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('/')
