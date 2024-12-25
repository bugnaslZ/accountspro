from django import forms
from .models import contactus
#class Contactusform(forms.Form):
 #   name = forms.CharField(max_length=220)
  #  email = forms.EmailField()
  #  subject = forms.CharField(max_length=220)
   # message = forms.CharField(widget=forms.Textarea({'rows':6}))

class Contactusform(forms.ModelForm):
    class Meta:
        model = contactus
        fields = ['name','email','subject','message']

        