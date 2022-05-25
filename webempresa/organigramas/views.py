from django.shortcuts import render
from .models import Post, Category

def organigramas(request):
    posts = Post.objects.all()
    return render(request, "organigramas/organigramas.html", {'posts':posts})