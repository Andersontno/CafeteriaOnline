from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.cafeteria.models import Produto
# Create your views here.

def index(request): 
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")
        return redirect('login')
    
    produto = Produto.objects.order_by("-data_criacao").filter(publicada=True)
    return render(request, 'cafeteria/index.html', {"cards": produto})

def imagem(request, imagem_id):
    produto = get_object_or_404(Produto, pk=imagem_id)
    return render(request, 'cafeteria/imagem.html', {"produto": produto})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado!")        
        return redirect('login')

    produto = Produto.objects.order_by("-data_criacao").filter(publicada=True)

    if "buscar" in request.GET:
        denominacao_a_buscar = request.GET["buscar"]
        if denominacao_a_buscar:
            produto = produto.filter(denominacao__icontains=denominacao_a_buscar)

    return render(request, "cafeteria/buscar.html", {"produto": produto})