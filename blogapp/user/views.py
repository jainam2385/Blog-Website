from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .validation import validate
from .forms import UserForm

def index(request):

    if request.method == "GET":
        return render(request, 'index.html', {})



def register(request):

    if request.method == "POST":
        user = UserForm(data = request.POST)

        if user.is_valid():
            print(user)

        return render(request, 'registration.html')

    return render(request, 'registration.html')



def login_user(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        
        else:
            return render(request, 'login.html', {"error": "Invalid username or password!"})
    
    return render(request, 'login.html', {})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


