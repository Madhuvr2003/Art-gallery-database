from django.shortcuts import render

# Create your views here.
def basic(request):
    return render(request,"basic.html")

def stockpicker(request):
    return render(request,"stockpicker.html")

def stocktracker(request):
    return render(request,"stocktracker.html")