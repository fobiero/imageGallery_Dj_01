from django.shortcuts import render
from .models import Category, Images, Location

# Create your views here.

def home(request):

    category = request.GET.get('category')
    if category == None:
        image = Images.objects.all()
    else:
        image = Images.objects.filter(category__name=category)
    # print(category)

    categories = Category.objects.all()
    # image = Images.objects.all()

    all_cat = {'categories': categories, 'image': image}

    return render(request, 'photos/home.html', all_cat)

def viewPhoto(request, pk):
    photo = Images.objects.get(id=pk)

    return render(request, 'photos/photo.html',{'photo': photo})
