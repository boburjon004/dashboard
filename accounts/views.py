from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return HttpResponse("Hello, world. You're at the dashboard.")
def contact(request):
    return HttpResponse("You're at the dashboard.")
def customuser(request):
    return HttpResponse("You're at the dashboard.")



