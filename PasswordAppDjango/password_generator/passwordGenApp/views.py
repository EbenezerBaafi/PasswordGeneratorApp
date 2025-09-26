from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random


# Create your views here.
def home(request):
    return render(request, 'home.html')

def password_gen(request):
    char = list('abcdefghijklmnopqrstuvwxyz')
    password = ''
    for i in range(14):
        password += random.choice(char)
    pas = {'password': password}
    return render(request, 'password.html', pas)