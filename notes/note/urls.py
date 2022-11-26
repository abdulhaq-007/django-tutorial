from django.urls import path
from . import views

app_name = 'note'

urlpatterns = [
    path('', views.NotesView.as_view(), name='home'),
    path('add/', views.AddNoteView.as_view(), name='add')
]