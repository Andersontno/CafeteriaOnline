from django.db import models

from datetime import datetime
# Create your models here.
class Produto(models.Model):

    OPCOES_CATEGORIA = [
        ("EXPRESSO", "Café Expresso")
        ,("CAPPUCCINO", "Cappuccino")
        ,("ROBUSTA", "Café Robusta")
        ,("EXTRAFORTE", "Café Extra Forte")
        ,("COMIDA", "Refeições")
    ]
    denominacao = models.CharField(max_length=100, null= False, blank=False)
    legenda = models.CharField(max_length=100, null= False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default="")
    descricao = models.TextField(null=False, blank=False)
    imagem = models.ImageField(upload_to="imagens/produto/", blank=True)
    publicada = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.denominacao
