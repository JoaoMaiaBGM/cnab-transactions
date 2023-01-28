from django.db.models import Sum

from cnab_api.models import CnabApiModel
from cnab_api.normalizers import FileNormalizer


class ApiRepository():
    def __init__(self):
        self.model = CnabApiModel
        self.normalizer = FileNormalizer()

    
    def create_transaction(self, normalizer):
        model = self.model(**normalizer)
        model.save()


    def get_transactions(self):
        query = self.model.objects.all().order_by('nome_loja')
        formatted_query = []
        for transaction in query:
            transaction = self.normalizer.query_normalizer(transaction)
            formatted_query = formatted_query + [transaction]
        return formatted_query


    def get_transactions_by_store_name(self, store_name):
        query = self.model.objects.filter(nome_loja=store_name).order_by('nome_loja')
        query_total = query.aggregate(Sum('valor'))
        query_total =  str(round(query_total['valor__sum'], 2))
        formatted_query = []
        for transaction in query:
            transaction = self.normalizer.query_normalizer(transaction)
            formatted_query = formatted_query + [transaction]
        return formatted_query, query_total