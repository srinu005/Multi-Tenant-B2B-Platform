from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Client, Invoice
from .serializers import ClientSerializer, InvoiceSerializer
from .tasks import process_invoice_notifications

class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        # 1. Row-level isolation is ALREADY handled by TenantManager!
        # 2. OPTIMIZATION: select_related performs a SQL JOIN
        return Invoice.objects.select_related('client').all()

    
    def perform_create(self, serializer):
        # 1. Save to DB (Fast)
        instance = serializer.save(tenant=self.request.tenant)
        
        # 2. Offload heavy work to Celery (Immediate / Non-blocking)
        # Instead of waiting 5 seconds, the API returns in milliseconds.
        process_invoice_notifications.delay(instance.id)
