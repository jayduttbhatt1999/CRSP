
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, ResearchCollaborationPost


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

class ResearchCollaborationPostForm(forms.ModelForm):
    class Meta:
        model = ResearchCollaborationPost
        fields = ['title', 'description', 'required_expertise', 'collaboration_format']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Title of your research article or your project'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'A brief description of your work'}),
            'required_expertise': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'The expertise and skills you needed'}),
            'collaboration_format': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Describe how you want to collaborate'}),
        }