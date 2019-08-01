from django.shortcuts import render
from .models import Pictures

# Create your views here.


def home(request):
    blog = Pictures.objects
    return render(request, 'blog/home.html', {'blog':blog})