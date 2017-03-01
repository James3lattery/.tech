from django.forms import ModelForm
from django import forms
from .models import note


class newNote(forms.ModelForm):

    class Meta:
        model = note
        fields = ('title', 'content')
