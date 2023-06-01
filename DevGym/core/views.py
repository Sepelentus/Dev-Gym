from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request, 'core/login.html')

def reserve(request):
    return render(request, 'core/reserva.html')
