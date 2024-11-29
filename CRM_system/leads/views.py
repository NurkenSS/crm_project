from django.shortcuts import render
from .models import Lead

def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/lead_list.html', {'leads': leads})

def lead_detail(request, pk):
    lead = Lead.objects.get(pk=pk)
    return render(request, 'leads/lead_detail.html', {'lead': lead})
