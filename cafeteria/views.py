from django.shortcuts import render
# Create your views here.

def index(request):

    dados = {
        1:{"Nome": "Cafe Expresso",
        "legenda": "Café Preto"},
        2:{"Nome": "Cafezão",
        "legenda": "Café Grande "},
        3:{"Nome": "Cafezin",
        "legenda": "Café Pequeno "},
    }
    
    return render(request, 'cafeteria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'cafeteria/imagem.html')