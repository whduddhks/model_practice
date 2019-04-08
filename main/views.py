from django.shortcuts import render
from .models import Blog
# Create your views here.

def home(request):
    posts = Blog.objects.all()
    return render(request, 'home.html', {'keyposts':posts})

