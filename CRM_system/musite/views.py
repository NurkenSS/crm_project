from .models import Service
from django.views.generic import CreateView, ListView

class ServiceCreateView(CreateView):
    model = Service
    fields = ['name', 'description', 'cost']
    template_name = 'service_create.html'
    success_url = '/success/'  

class ServiceListView(ListView):
    model = Service
    template_name = 'service_list.html'
    context_object_name = 'services'
