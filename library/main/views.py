from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Book, Category, Author

# class BookTemplateView(TemplateView):
#     template_name = 'books.html'

class BookListView(ListView):
    model = Book
    template_name = 'books.html'

class BookDetailView(DetailView):
    model = Book  
    template_name = 'book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.all()
        return context
