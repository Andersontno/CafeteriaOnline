from django.shortcuts import render, get_object_or_404
from cafeteria.models import Produto
# Create your views here.

def index(request): 
    produto = Produto.objects.filter(publicada=True)
    return render(request, 'cafeteria/index.html', {"cards": produto})

def imagem(request, imagem_id):
    produto = get_object_or_404(Produto, pk=imagem_id)
    return render(request, 'cafeteria/imagem.html', {"produto": produto})