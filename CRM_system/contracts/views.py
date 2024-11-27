from django.shortcuts import render
from .models import Contract

def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'contracts/contract_list.html', {'contracts': contracts})

def contract_detail(request, pk):
    contract = Contract.objects.get(pk=pk)
    return render(request, 'contracts/contract_detail.html', {'contract': contract})
