from django.urls import path
from apps.cafeteria.views import *

urlpatterns = [
    path('', index, name = "index"),
    path('imagem/<int:imagem_id>', imagem, name = "imagem"),
    path('buscar', buscar, name="buscar")
]
