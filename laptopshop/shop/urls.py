from django.urls import path
from .import views
app_name = 'shop'

urlpatterns = [
    path('', views.HopePageView.as_view(), name='home')
]
