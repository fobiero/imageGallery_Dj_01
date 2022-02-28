
from django.db import models

# Create your models here.

from . import views

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Images(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.description


class Location(models.Model):
    image = models.ForeignKey(Images, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.image


