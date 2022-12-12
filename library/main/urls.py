from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('detail/<int:pk>/', views.BookDetailView.as_view(), name='book_detail')
    path('category/<slug:slug>/', views.CategoryListView.as_view(), name='cat_list')
]