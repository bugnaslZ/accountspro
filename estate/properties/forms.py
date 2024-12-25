from django import forms
from .models import Commentt
class Comment(forms.ModelForm):
    
    class Meta:
        model = Commentt
        fields = ['name','comment']

        