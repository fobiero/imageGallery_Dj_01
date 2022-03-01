from django.shortcuts import render
from .models import Category, Images, Location

# Create your views here.

def home(request):
    categories = Category.objects.all()
    image = Images.objects.all()

    all_cat = {'categories': categories, 'image': image}

    return render(request, 'photos/home.html', all_cat)

def viewPhoto(request, pk):
    photo = Images.objects.get(id=pk)

    return render(request, 'photos/photo.html',{'photo': photo})
