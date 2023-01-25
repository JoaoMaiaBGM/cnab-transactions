from django.db import models


class CnabApiModel(models.Model):
    tipo = models.IntegerField(blank=False, null=False, min=1, max=9, max_length=1)
    data = models.DateField(blank=False, null=False)
    valor = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    cpf = models.CharField(blank=False, null=False, max_length=11)
    cartao = models.CharField(blank=False, null=False, max_length=12)
    hora = models.TimeField(blank=False, null=False)
    dono_da_loja = models.CharField(blank=False, null=False, max_length=14)
    nome_loja = models.CharField(blank=False, null=False, max_length=19)