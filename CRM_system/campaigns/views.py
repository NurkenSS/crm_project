from django.shortcuts import render
from .models import Campaign

def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'campaign_list.html', {'campaigns': campaigns})
