from django import forms
from django.contrib.admin import widgets

from .models import BlogPost

class BlogPostForm(forms.Form):
    title   = forms.CharField(max_length=255)
    slug    =  forms.SlugField()
    contect = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model =  BlogPost
        fields = [
            "title",
            "image",
            "slug",
            "content",
            "publish_date"
            ]