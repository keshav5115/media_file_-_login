from django import forms
from .models import Register
class registerform(forms.ModelForm):
    password2=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Register
        fields=['username','first_name','last_name','email','phone','password']
    