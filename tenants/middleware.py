from .models import Organization
from .utils import set_current_tenant


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. Get the host (e.g., 'apple.localhost:8000')
        host = request.get_host().split(":")[0]
        parts = host.split(".")

        # 2. Logic: If there is a subdomain (e.g., 'apple')
        if len(parts) > 1:
            subdomain = parts[0]
            try:
                # Find the Organization by its slug
                tenant = Organization.objects.get(slug=subdomain, is_active=True)
                set_current_tenant(tenant)
                request.tenant = tenant  # Attach it to the request object too
            except Organization.DoesNotExist:
                set_current_tenant(None)
                request.tenant = None
        else:
            set_current_tenant(None)
            request.tenant = None

        response = self.get_response(request)
        return response
