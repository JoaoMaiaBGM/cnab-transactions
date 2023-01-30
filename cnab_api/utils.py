import datetime

from cnab_api.models import CnabApiModel


class FileNormalizer():
    
    def file_normalizer(self, value):
        if value is not None:
            return {
                'tipo': value[0:1],
                'data': datetime.datetime(int(value[1:5]), int(value[5:7]), int(value[7:9])),
                'valor': self.transactions_signal(int(value[0:1]), float(value[9:19]) / -100.00),
                'cpf': value[19:30],
                'cartao': value[30:42],
                'hora': datetime.time(int(value[42:44]), int(value[44:46]), int(value[46:48])),
                'dono_da_loja': value[48:62],
                'nome_loja': value[62:81],
            }
            

    def transactions_signal(self, type_transactions, value):
        if type_transactions in [2,3,9]:
            return value
        else:
            return abs(value)


    def type_transactions(self, type_transaction):

        if type_transaction == 1:
            return 'Débito'
        elif type_transaction == 2:
            return 'Boleto'
        elif type_transaction == 3:
            return 'Financiamento'
        elif type_transaction == 4:
            return 'Crédito'
        elif type_transaction == 5:
            return 'Recebimento Empréstimo'
        elif type_transaction == 6:
            return 'Vendas'
        elif type_transaction == 7:
            return 'Recebimentos TED'
        elif type_transaction == 8:
            return 'Recebimentos DOC'
        elif type_transaction == 9:
            return 'Aluguel'

    
    def query_normalizer(self, query):
         if query is not None:
            return {
                'tipo': self.type_transactions(query.tipo),
                'data': query.data,
                'valor': query.valor,
                'cpf': query.cpf,
                'cartao': query.cartao,
                'hora': query.hora,
                'dono_da_loja': query.dono_da_loja,
                'nome_loja': query.nome_loja,
            }

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