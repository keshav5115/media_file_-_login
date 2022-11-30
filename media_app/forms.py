from django import forms
from media_app.models import Register
class Registerform(forms.ModelForm):
    class Meta:
        model=Register
        fields='__all__'
        widgets={'name':forms.TextInput,
                'phone':forms.NumberInput,
                'email':forms.EmailInput,
                'sal':forms.NumberInput,
                # 'gender':forms.ChoiceField,
                'date':forms.DateInput,
                'photo':forms.FileInput,
                'resume':forms.FileInput}