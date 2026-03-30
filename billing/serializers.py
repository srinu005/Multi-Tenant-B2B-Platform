from rest_framework import serializers
from .models import Client, Invoice


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name", "email"]


class InvoiceSerializer(serializers.ModelSerializer):
    # We include the client name to show how optimization works
    client_name = serializers.CharField(source="client.name", read_only=True)

    class Meta:
        model = Invoice
        fields = ["id", "client", "client_name", "amount", "description", "created_at"]
