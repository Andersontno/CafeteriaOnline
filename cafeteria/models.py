from django.db import models

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
    imagem = models.CharField(max_length=100, null= False, blank=False)

    def __str__(self):
        return f"Produto [denominacao={self.denominacao}]"
