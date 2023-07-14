
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    dept = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    scholar = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('email', 'password', 'password1', 'name', 'dept', 'scholar')


class CommentForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "placeholder": "Add your comment"}), label="")

    class Meta:
        model = Comment
        fields = ['body']


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ['body']