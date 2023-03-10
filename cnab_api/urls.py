from django.urls import path

from .views import CnabAPIView, CnabFileTransactionsDetail, CnabFormView

urlpatterns = [
    path('cnab/', CnabAPIView.as_view()),
    path('cnab/<str:nome_loja>', CnabAPIView.as_view()),
    path('cnab_file/', CnabFormView.as_view()),
    path('cnab_file/transactions/', CnabFileTransactionsDetail.as_view()),
]
