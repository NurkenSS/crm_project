from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'status', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('status',)
    ordering = ('-created_at',)
