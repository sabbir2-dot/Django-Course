from django.shortcuts import render, redirect
from posts.models import Post
from categories.models import Category
def home(request, category_slug = None):
    data = Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Post.objects.filter(category = category)
    categories = Category.objects.all()
    print(data)
    return render(request, 'home.html', {'data':data, 'category' : categories})