from django import forms
from .models import *
from django.forms import TextInput

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("author", "title", "body", 'category')
        widgets = {
            'author': TextInput(attrs={
                'class' : "form-control",
                'placeholder' : "제목을 작성하세요",
            }),
        }