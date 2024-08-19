from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    cpf=forms.CharField(
        label="CPF",
        required=True,
        max_length=14,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "loginCPF",
                "placeholder": "CPF",
                "inputmode": 'numeric',
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "loginSenha",
                "placeholder": "Senha"
            }
        )
    )