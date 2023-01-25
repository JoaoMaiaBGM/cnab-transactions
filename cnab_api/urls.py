from django.urls import path

from .views import CnabFormView

urlpatterns = [
    path('cnab_file/', CnabFormView.as_view())
]