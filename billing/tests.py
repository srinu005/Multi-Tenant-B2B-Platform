# Create your tests here.
import pytest
from django.urls import reverse
from .models import Client, Invoice


@pytest.mark.django_db
class TestMultiTenancy:
    def test_tenant_isolation(self, api_client, tenant_apple, tenant_google):
        """
        CRITICAL TEST: Ensure Apple cannot see Google's invoices.
        """
        # 1. Create an invoice for Apple
        Client.objects.create(tenant=tenant_apple, name="Apple Client", email="a@a.com")
        apple_client = Client.all_objects.get(name="Apple Client")
        Invoice.objects.create(
            tenant=tenant_apple,
            client=apple_client,
            amount=100,
            description="Apple Bill",
        )

        # 2. Access via Apple Subdomain
        api_client.credentials(HTTP_HOST="apple.localhost")
        url = reverse("invoice-list")
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data["results"]) == 1

        # 3. Access via Google Subdomain (Should be EMPTY)
        api_client.credentials(HTTP_HOST="google.localhost")
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data["results"]) == 0

    def test_async_task_trigger(self, api_client, tenant_apple, mocker):
        """
        Ensures Celery task is called (reducing latency).
        """
        # Mock the celery task so we don't actually wait 5 seconds
        mock_task = mocker.patch("billing.tasks.process_invoice_notifications.delay")

        api_client.credentials(HTTP_HOST="apple.localhost")
        client = Client.objects.create(
            tenant=tenant_apple, name="Test", email="t@t.com"
        )

        url = reverse("invoice-list")
        data = {"client": client.id, "amount": "50.00", "description": "Test Task"}

        response = api_client.post(url, data)

        assert response.status_code == 201
        # Prove the task was offloaded to background
        assert mock_task.called


@pytest.mark.django_db
def test_invoice_task_logic(tenant_apple):
    from billing.tasks import process_invoice_notifications

    client = Client.objects.create(
        tenant=tenant_apple, name="TaskTest", email="t@t.com"
    )
    invoice = Invoice.objects.create(
        tenant=tenant_apple, client=client, amount=10, description="Test"
    )

    result = process_invoice_notifications(invoice.id)
    assert "Success" in result


@pytest.mark.django_db
def test_tenant_not_found(api_client):
    """
    Triggers lines 21-26 in middleware by using a fake subdomain.
    """
    api_client.credentials(HTTP_HOST="nonexistent.localhost")
    url = reverse("invoice-list")
    response = api_client.get(url)

    # It should return 200 (or 404 depending on your logic),
    # but most importantly, it executes the 'DoesNotExist' block.
    assert response.status_code == 200
    assert len(response.data["results"]) == 0
