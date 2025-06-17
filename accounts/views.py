from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect('todo:home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('todo:home')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, "user dosn't exist")
        else:
                messages.error(request, "invalid data try again please")

        return redirect('accounts:login')
    
    return render(request, 'accounts/login.html')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('todo:home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.error(request, "This name already exists")
            return redirect('accounts:signup')

        if len(password) < 6:
            messages.error(request, "Password must be at least 6 characters.")
            return redirect('accounts:signup')

        if User.objects.filter(email=email).exists():
            messages.error(
                request, "An account with this email already exists.")
            return redirect('accounts:signup')

        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)

        return redirect('todo:home')

    return render(request, 'accounts/signup.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You've been logged out successfully.")
    return redirect('accounts:login')