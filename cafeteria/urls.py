from django.urls import path
from cafeteria.views import *

urlpatterns = [
    path('', index),
    path('imagem/', imagem),
    path('imagem.html', imagem)
]
