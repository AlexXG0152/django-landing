from .models import Author, Post, Feedback
from django.template.defaultfilters import slugify
from django import forms
 
class FeedbackForm(forms.ModelForm):
 
    class Meta:
        model = Feedback
        fields = '__all__'
