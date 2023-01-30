from django.urls import path

from .views import CnabFileTransactions, CnabFormView

urlpatterns = [
    path('cnab_file/', CnabFormView.as_view()),
    path('cnab_file/transactions/', CnabFileTransactions.as_view()),
]