from django import forms
from movie.models import moviemodel

class movieform(forms.Form):
    class Meta:
        model=moviemodel
        fields='__all__'
