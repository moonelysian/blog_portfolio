from django import forms
from .models import Blogapp

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blogapp
        fields = ['title' , 'body']