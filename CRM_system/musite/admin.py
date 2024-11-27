from django.contrib import admin
from .models import Service # type: ignore

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'cost')  
admin.site.register(Service, ServiceAdmin) 