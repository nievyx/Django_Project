from django.shortcuts import render
from .models import Post

# Create your views here.
# Handle web requests and return HTML responses here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})