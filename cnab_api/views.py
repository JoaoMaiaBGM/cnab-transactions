from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView

from cnab_api.forms import StoreFilter, UploadFileForm
from cnab_api.models import CnabApiModel
from cnab_api.utils import FileUtils


class CnabFormView(FormView):
    template_name = 'index.html'
    form_class = UploadFileForm
    success_url=('transactions/')
    read_file = FileUtils()            


    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        form_class = self.get_form_class()
        file = self.get_form(form_class)
        files = request.FILES.get('file')

        if file.is_valid():
            print('Arquivo válido')
            file = files.read()
            self.read_file.read_file(file)
            return self.form_valid(file)
        else:
            print('Arquivo inválido')
            return self.form_invalid(file)

    
class CnabFileTransactions(FormView):
    store_name = None
    form_class = StoreFilter
    template_name = "transactions.html"
    success_url=('/cnab_file/transactions/')
    filter = FileUtils()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transactions'], context['total_sum'] = self.filter.filter(self.store_name)
        context['store_names'] = CnabApiModel.objects.all().values('nome_loja').distinct()
        return context

    def form_valid(self, form):
        return super().form_valid(form)
    
    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        context = super().get_context_data(**kwargs)
        form_class = self.get_form_class()
        file = self.get_form(form_class)

        if file.is_valid():
            print('Arquivo válido')
            self.store_name = file.cleaned_data['store']
            context['transactions'], context['total_sum'] = self.filter.filter(self.store_name)
            return self.render_to_response(context)
        else:
            print('Arquivo inválido')
            return self.form_invalid(file)