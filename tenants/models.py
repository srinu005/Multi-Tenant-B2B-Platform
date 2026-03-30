from django.db import models
from .utils import get_current_tenant

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



class TenantManager(models.Manager):
    """
    This Manager ensures that any query (e.g. Invoice.objects.all())
    ONLY returns data belonging to the current tenant in the middleware.
    """
    def get_queryset(self):
        tenant = get_current_tenant()
        return super().get_queryset().filter(tenant=tenant)
class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Organization, on_delete=models.CASCADE)
    
    # The 'objects' manager is now tenant-aware!
    objects = TenantManager()
    # We keep a 'plain' manager just in case we need to see everything (e.g. for Admin)
    all_objects = models.Manager() 

    class Meta:
        abstract = True