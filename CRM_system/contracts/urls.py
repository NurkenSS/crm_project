from django.urls import path
from .views import ContractCreateView, ContractListView

urlpatterns = [
    path('add/', ContractCreateView.as_view(), name='contract_create'),
    path('list/', ContractListView.as_view(), name='contract_list'), 
]
