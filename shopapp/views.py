from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def images(request):
    return render(request, 'gallery.html')

