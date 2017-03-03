from django.forms import ModelForm
from django import forms
from .models import note, image


class newNote(forms.ModelForm):

    class Meta:
        model = note
        fields = ('title', 'content')


class uploadImage(forms.ModelForm):

    class Meta:
        model = image
        fields = ('image',)
