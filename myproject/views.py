from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def header(request):
    return render(request,'layout/header.html')

def index(request):
    return render(request,'layout/index.html')

def footer(request):
    return render(request,'layout/footer.html')
