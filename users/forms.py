from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Логин",
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': "Имя",
                   }
        )
    )
    password = forms.CharField(
        label='Пароль',
        max_length=40,
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Пароль'
                   }
        )
    )
