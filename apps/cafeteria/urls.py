from django.urls import path
from apps.cafeteria.views import *

urlpatterns = [
    path('', index, name = "index"),
    path('imagem/<int:imagem_id>', imagem, name = "imagem"),
    path('buscar', buscar, name="buscar"),
    path('cadastrar_produto', cadastrar_produto, name="cadastrar_produto"),
    path('editar_produto/<int:produto_id>', editar_produto, name="editar_produto"),
    path('deletar_produto', deletar_produto, name="deletar_produto"),

]
