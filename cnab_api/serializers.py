from django.db.models import Sum
from rest_framework import serializers

from .models import CnabApiModel


class CnabApiSerializer(serializers.ModelSerializer):
    total_sum = serializers.SerializerMethodField()

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
            "total_sum",
        ]

    @classmethod
    def get_total_sum(cls, instance):
        total_sum = CnabApiModel.objects.all().aggregate(Sum("valor"))
        return total_sum
