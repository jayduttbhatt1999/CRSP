from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    dept = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    scholar = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('email', 'password', 'password1', 'name', 'dept', 'scholar')


# email,password, password1, name, dept, scholar