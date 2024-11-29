from django.shortcuts import render
from .models import Client

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = Client.objects.get(pk=pk)
    return render(request, 'clients/client_detail.html', {'client': client})
