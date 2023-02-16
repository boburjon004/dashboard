from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, 'accounts/dashboard.html')


def products(request):
    return render(request, 'accounts/products.html')


def customuser(request):
    return render(request, 'accounts/customer.html')



