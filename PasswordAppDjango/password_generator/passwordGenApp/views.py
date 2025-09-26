from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random


# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to your number one password generator app!!</h1> <br>, <h2>Go to /password to generate a password</h2>")

def pasword_gen(request):
    char = list('abcdefghijklmnopqrstuvwxyz')
    password = ''
    for i in range(14):
        password += random.choice(char)
    pas = {'password': password}
    return JsonResponse(pas)