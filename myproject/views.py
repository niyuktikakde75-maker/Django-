from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def header(request):
    return render(request,'header.html')
