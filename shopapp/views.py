from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def images(request):
    return render(request, 'gallery.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    return render(request, 'registration.html')

def products(request):
    return render(request, 'products.html')

