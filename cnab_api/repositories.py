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