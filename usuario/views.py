from django.shortcuts import render
from usuario.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms()
    return render(request, 'usuario/login.html', {"form":form})

def cadastro(request):
    form = CadastroForms()
    return render(request, 'usuario/cadastro.html', {"form":form})


def logout(request):
    pass
    