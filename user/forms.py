from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm

from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '������� �����'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': '������� ������'
    }))

    class Meta:
        model = User
        fields = ["username", "password"]


class UserProfileForm(UserChangeForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '������� ���'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '������� �������'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'readonly': True
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']