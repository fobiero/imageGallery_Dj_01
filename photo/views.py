from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'photos/home.html')

def viewPhoto(request, pk):
    return render(request, 'photos/photo.html')