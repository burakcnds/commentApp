from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name','email','text',]


        widgets = {
            'full_name':forms.TextInput(attrs={'class':'form-control  border border-1 border-black mb-2'}),
            'email':forms.EmailInput(attrs={'class':'form-control  border border-1 border-black mb-2'}),
        }