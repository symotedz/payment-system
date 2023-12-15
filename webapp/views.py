from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm


# Create your views here.
def webapp_index(request):
    return render(request, "index.html")



def register(request):
    form = RegistrationForm(request.POST)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webapp_index')  # Create a success page or redirect as needed
    else:
        form = RegistrationForm(request.POST)

    return render(request, 'register.html', {'form': form})
