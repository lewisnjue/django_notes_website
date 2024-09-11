from .models import notes
from django import forms
class NoteForm(forms.ModelForm):
    class Meta:
        model = notes
        fields = ['title','body']