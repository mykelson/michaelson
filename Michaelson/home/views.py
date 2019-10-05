from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPosts

# Create your views here.
def index(request):
    return render(request, "home/index.htm")

def about(request):
    return render(request, "home/about.htm")

def contact(request):
    return render(request, "home/contact.htm")

def blog(request):
    context = {
        "blogPosts": BlogPosts.objects.all()
    }
    return render(request, "home/blog.htm", context)

def vlog(request):
    return render(request, "home/vlog.htm")