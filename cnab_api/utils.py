from cnab_api.models import CnabApiModel
from cnab_api.normalizers import FileNormalizer


class FileUtils():

    def __init__(self):
        self.normalizer = FileNormalizer()
        self.model = CnabApiModel


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


    def read_file(self, file):
        file = file.decode('utf-8')
        for value in file.splitlines():
            normalizer = self.normalizer.file_normalizer(value)
            self.create_transaction(normalizer)
        return file


    def filter(self, store):
        return self.get_transactions(), None