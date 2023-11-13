from django.db import models

# Create your models here.
class Produto(models.Model):
    denominacao = models.CharField(max_length=100, null= False, blank=False)
    legenda = models.CharField(max_length=100, null= False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    imagem = models.CharField(max_length=100, null= False, blank=False)

    def __str__(self):
        return f"Produto [denominacao={self.denominacao}]"
