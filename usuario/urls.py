from django.urls import path
from usuario.views import *

urlpatterns = [
    path('login', login, name = "login"),
    path('cadastro', cadastro, name="cadastro")
]
