from django import forms 

class LoginForms(forms.Form):
    login = forms.CharField(
        label = "Login",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
                ,"placeholder": "Ex: Cupcake"
            }
        )
    )
    senha = forms.CharField(
        label = "Senha",
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
                ,"placeholder": "Digite sua senha"
            }
        )
    )
     
class CadastroForms(forms.Form):
    nome = forms.CharField(
        label = "Nome Completo",
        max_length=250,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
                ,"placeholder": "Ex: Lucas da Silva"
            }
        )
    )
    email = forms.EmailField(
        label = "Email",
        max_length=250,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
                ,"placeholder": "Ex: exemplo@exemplo.com"
            }
        )
    )
    senha = forms.CharField(
        label = "Senha",
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
                ,"placeholder": "Digite sua senha"
            }
        )
    )
    senha_confirmacao = forms.CharField(
        label = "Confirmação de Senha",
        max_length=70,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
                ,"placeholder": "Digite sua senha novamente"
            }
        )
    )
     
