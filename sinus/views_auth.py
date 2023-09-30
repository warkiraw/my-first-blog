from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import Transaction

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if User.objects.filter(username=email).exists():
            message = 'Пользователь с таким Email уже существует'
            return render(request, 'registration.html', {'message': message})
        if password == password2:
            try:
                user = User.objects.create_user(username=email, password=password)
                user.first_name = username
                user.email = email
                user.save()
                user = authenticate(username=email, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect("/")
            except :
                message = 'Ошибка регистрации'
                return render(request, 'registration.html', {'message': message})
        else:
            message = 'Пароли не совпадают'
            return render(request, 'registration.html', {'message': message})
    else:
        return render(request, 'registration.html')
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            message = 'Неверный логин или пароль'
            return render(request, 'login.html', {'message': message})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("/")
def index(request):
    if request.user.is_authenticated:
        return redirect('/account')
    else:
        return render(request, 'index.html')
def account(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("/")

    transactions = Transaction.objects.filter()
    return render(request, 'base.html', {"transactions": transactions})