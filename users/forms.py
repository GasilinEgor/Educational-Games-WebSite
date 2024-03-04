from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        help_text='Придумайте себе уникальный логин!'
    )

    email = forms.EmailField(
        label='Email'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')
