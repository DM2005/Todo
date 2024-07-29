from django.shortcuts import render

def login(request):
    return render(request,"accounts/login.html")

# Create your views here.
