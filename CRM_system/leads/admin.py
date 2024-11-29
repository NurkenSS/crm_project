from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'status', 'campaign', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('status', 'campaign')
    ordering = ('created_at',)
