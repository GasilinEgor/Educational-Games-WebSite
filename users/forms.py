from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
        max_length=50,
        help_text='Придумайте себе уникальный логин!'
    )

    email = forms.EmailField(
        label='Email'
    )

    name = forms.CharField(
        label='Имя',
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    surname = forms.CharField(
        label='Фамилия',
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
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
                   'placeholder': "Логин",
                   }
        )
    )
    password = forms.CharField(
        label='Пароль',
        max_length=40,
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Пароль',
                   }
        )
    )


class CreateGroupForm(forms.Form):
    name = forms.CharField(
        label='Название',
        max_length=31,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Название',
                   }
        )
    )

    slogan = forms.CharField(
        label='Слоган',
        max_length=127,
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'placeholder': 'Слоган'}
        )
    )

    description = forms.CharField(
        label='Описание',
        max_length=2047,
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'placeholder': 'Описание'}
        )
    )
