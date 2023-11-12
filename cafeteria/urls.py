from django.urls import path
from cafeteria.views import *

urlpatterns = [
    path('', index, name = "index"),
    path('imagem/', imagem, name = "imagem"),
]
