from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('detail/<slug:post_slug>', views.postDetailView, name='post_detail'),
    path('results/',views.resultPageView , name = 'result_page')
]