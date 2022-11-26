from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Notes, Status, Category
from .forms import AddNoteForm

# Create your views here.

class NotesView(ListView):
    """Hamma note lardi chiqaradigan view"""
    model = Notes


class AddNoteView(View):
    """! ta note di alohida korsatadigan view"""

    template_name = 'note/add.html'

    def get(self, request, *args, **kwargs):
        form = AddNoteForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if form.is_valid():
                form.save()
            return redirect("/")    
        else:
            return(request, self.template_name)    
        return render(request, self.template_name, {'form': form})
    
