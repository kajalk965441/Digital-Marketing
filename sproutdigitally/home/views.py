from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{})

def company(request):
    return render(request,'company.html',{})

def expertise(request):
    return render(request,'expertise.html',{})

def contact(request):
    return render(request,'contact.html',{})