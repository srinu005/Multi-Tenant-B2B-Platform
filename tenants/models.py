from django.db import models

# Create your models here.
from django.db import models

class Organization(models.Model):
    """
    This represents the 'Tenant' (the B2B Client).
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, help_text="Used for routing (e.g., client-a.platform.com)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TenantAwareModel(models.Model):
    """
    ABSTRACT MODEL: Every B2B model in our system (Invoices, Tasks, etc.) 
    will inherit from this to ensure it is tied to an Organization.
    """
    tenant = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        abstract = True