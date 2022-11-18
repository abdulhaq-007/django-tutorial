from django.shortcuts import render
from .models import Tag, Post
from django.db.models import Q
# Create your views here.


def homePageView(request):
    all_posts = Post.objects.all()
    data = {
        'all_posts': all_posts,
    }
    return render(request, 'index.html', context=data)


def postDetailView(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    related_posts = Post.objects.filter(tag=post.tag.all()[0])

    data = {
        "post": post,
        "related_posts": related_posts
    }
    return render(request, 'post.html', context=data)

def searchView(request):
    query = request.GET.get('search_query')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))

    context = {
        'posts': posts,
    }
    return render(request, 'results.html', context)

