from django.shortcuts import render
from django.views.generic import TemplateView
from .models import User
# Create your views here.
class ProfileView(TemplateView):
    template_name = 'registration/profile.html'