from threading import local

# This creates a thread-local storage to keep the tenant safe 
# even when multiple users hit the server at once.
_thread_locals = local()

def set_current_tenant(tenant):
    _thread_locals.tenant = tenant

def get_current_tenant():
    return getattr(_thread_locals, "tenant", None)