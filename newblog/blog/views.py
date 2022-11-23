from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, TemplateView
# Create your views here.

class PostTemplateView(TemplateView):
    template_name = "index.html"


class PostListView(ListView):
    model = Post
    template_name = "index.html"
