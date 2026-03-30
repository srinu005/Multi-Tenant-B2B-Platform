import time
from celery import shared_task
from .models import Invoice

@shared_task
def process_invoice_notifications(invoice_id):
    """
    Simulates a heavy task (Generating PDF, Sending Email)
    that would normally slow down the API.
    """
    try:
        invoice = Invoice.objects.get(id=invoice_id)
        print(f"--- STARTING HEAVY PROCESSING FOR INVOICE {invoice_id} ---")
        
        # Simulate 5 seconds of work (Invoicing/Emails)
        time.sleep(5) 
        
        print(f"--- EMAIL SENT TO {invoice.client.email} ---")
        return f"Success for Invoice {invoice_id}"
    except Invoice.DoesNotExist:
        return "Invoice not found"