from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def index(request):
    return render(request,'base.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

    
    

