from django import forms

from .models import BlogPost

class BlogPostForm(forms.Form):
    title   = forms.CharField(max_length=255)
    slug    =  forms.SlugField()
    contect = forms.CharField(widget=forms.Textarea)
    