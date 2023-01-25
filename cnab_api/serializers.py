from rest_framework import serializers

from .models import CnabApiModel


class CnabApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = CnabApiModel
        fields = [
            'tipo',
            'data',
            'valor',
            'cpf',
            'cartao',
            'hora',
            'dona_da_loja',
            'nome_loja',
        ]