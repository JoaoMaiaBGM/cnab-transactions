import datetime

from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView

from .forms import UploadFileForm


class CnabFormView(FormView):
    template_name = 'index.html'
    form_class = UploadFileForm
    success_url=('cnab_file/transactions/')
    

    def file_normalizer(self, file, value):
        for value in file.splitlines():
            return {
                'tipo': value[0:1],
                'data': datetime.date(int(value[0:1]), int(value[5:7]), int(value[7:9])),
                'valor': self.transactions_signal(int(value[0:1]), float(value[9:19]) / 100),
                'cpf': value[19:30],
                'cartao': value[30:42],
                'hora_transacao': datetime.time(int(value[42:48]), int(value[44:46]), int(value[46:48])),
                'dono_loja': value[48:62],
                'nome_loja': value[62:81],
            }
            

    def transactions_signal(self, type_transactions, value):
        if type_transactions in [2,3,9]:
            return value
        else:
            return abs(value)


    def type_transactions_list(self, type_transaction):

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
        else:
            return 'Aluguel'

    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.get('form')

        if form.is_valid():
            print('Formulário válido')
            file = files.read()
            self.file_normalizer(file)
            return self.form_valid(form)
        else:
            print('Formulário inválido')
            return self.form_invalid(form)

    
class CnabFileTransactions(FormView):
    template_name = "transactions.html"
    success_url=('/cnab_file/transactions/')
    
    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            print('Formulário válido')
            return self.form_valid(form)
        else:
            print('Formulário inválido')
            return self.form_invalid(form)