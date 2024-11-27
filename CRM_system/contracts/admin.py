from django.contrib import admin
from .models import Contract

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'start_date', 'end_date', 'amount', 'status', 'created_at')
    search_fields = ('name', 'client__name', 'amount')
    list_filter = ('status', 'client')
    ordering = ('-created_at',)
