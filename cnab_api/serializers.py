from django.db.models import Sum
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
            'dono_da_loja',
            'nome_loja',
            'total_sum',
        ]

    
    def get_total_sum(self, instance):
        total_sum = CnabApiModel.objects.all().aggregate(Sum('valor'))
        return total_sum