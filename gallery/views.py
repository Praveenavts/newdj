from django.shortcuts import render
from .models import HomeImage


def home(request):
    images = HomeImage.objects.all()
    return render(request, 'gallery/home.html', {'images': images})
