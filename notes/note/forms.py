from django import forms
from .models import Notes

class AddNoteForm(forms.ModelForm):
    """Forma qoshish"""
    class Meta:
        model = Notes
        fields = "__all__"

        