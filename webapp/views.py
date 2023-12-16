from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login

from . models import UserProfile


# Create your views here.
def webapp_index(request):
    users = UserProfile.objects.all()
    context = {
        'users' : users
    }
    return render(request, "index.html", context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('webapp_index')  # redirecting to the index page
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def register(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')  # Create a success page or redirect as needed
    else:
        form = RegistrationForm(request.POST)

    return render(request, 'register.html', {'form': form})


