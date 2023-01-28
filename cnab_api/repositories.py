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
        normalized_query = []
        for transaction in query:
            transaction = self.normalizer.query_normalizer(transaction)
            normalized_query = normalized_query + [transaction]
        return normalized_query


    def get_transactions_by_store(self, store):
        query = self.model.objects.filter(nome_loja=store).order_by('nome_loja')
        query_total = query.aggregate(Sum('valor'))
        query_total =  str(round(query_total['valor__sum'], 2))
        normalized_query = []
        for transaction in query:
            transaction = self.normalizer.query_normalizer(transaction)
            normalized_query = normalized_query + [transaction]
        return normalized_query, query_total