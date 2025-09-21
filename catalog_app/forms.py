from django import forms
from .models import Artiste, Song, Lyric

class ArtisteForm(forms.ModelForm):
    class Meta:
        model = Artiste
        fields = ['first_name', 'last_name', 'age']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'age': forms.NumberInput(attrs={'class': 'form-input'}),
        }

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'release_date', 'artiste']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'release_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'artiste': forms.Select(attrs={'class': 'form-select'}),
        }

class LyricForm(forms.ModelForm):
    class Meta:
        model = Lyric
        fields = ['content', 'song']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 10}),
            'song': forms.Select(attrs={'class': 'form-select'}),
        }
