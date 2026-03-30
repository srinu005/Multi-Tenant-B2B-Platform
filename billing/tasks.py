from celery import shared_task
from .models import Invoice
import time


@shared_task
def process_invoice_notifications(invoice_id):
    try:
        # We use all_objects because the Celery worker
        # doesn't have the Tenant Middleware active
        invoice = Invoice.all_objects.get(id=invoice_id)
        time.sleep(1)  # Simulate work
        return f"Success for Invoice {invoice_id}"
    except Invoice.DoesNotExist:
        return "Invoice not found"
