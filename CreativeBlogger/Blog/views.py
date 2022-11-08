from django.http import HttpResponse
from django.shortcuts import render
from Blog.models import Post, Category

# Create your views here.
#from CreativeBlogger.Blog.models import Category


def home(request):
    #load all the post from db
    posts = Post.objects.all()[:10]
    print(posts)
    #print posts

    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats

    }

    return render(request, 'home.html', data)

def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})

def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})
