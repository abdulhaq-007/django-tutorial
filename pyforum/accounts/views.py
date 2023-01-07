from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView
from django.views.generic import UpdateView
from django.contrib.auth.forms import UserCreationForm
from .models import User
# Create your views here.


class ProfileView(TemplateView):
    template_name = 'registration/profile.html'

class ProfileEditView(UpdateView):
    model = User
    template_name = 'registration/user_form.html'
    fields = ['first_name', 'last_name', 'image', 'bio', 'address',
     'facebook_link', 'instagram_link', 'telegram_link']
    success_url = reverse_lazy("accounts:profile")

def register(request):
    return render(request, 'registration/register.html')    