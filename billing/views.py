from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Client, Invoice
from .serializers import ClientSerializer, InvoiceSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        # 1. Row-level isolation is ALREADY handled by TenantManager!
        # 2. OPTIMIZATION: select_related performs a SQL JOIN
        return Invoice.objects.select_related('client').all()

    def perform_create(self, serializer):
        # Automatically assign the invoice to the current tenant from the request
        serializer.save(tenant=self.request.tenant)