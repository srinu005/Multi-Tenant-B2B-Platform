import pytest
from rest_framework.test import APIClient
from tenants.models import Organization
import django



@pytest.fixture
def api_client():
    """Provides a DRF API client for testing."""
    return APIClient()


@pytest.fixture
def tenant_apple(db):
    """Creates a test tenant for Apple."""
    # Use get_or_create to avoid duplicate key errors during test runs
    obj, _ = Organization.objects.get_or_create(
        slug="apple", defaults={"name": "Apple Inc"}
    )
    return obj


@pytest.fixture
def tenant_google(db):
    """Creates a test tenant for Google."""
    obj, _ = Organization.objects.get_or_create(
        slug="google", defaults={"name": "Google LLC"}
    )
    return obj


@pytest.fixture(autouse=True)
def set_celery_eager(settings):
    settings.CELERY_TASK_ALWAYS_EAGER = True
    settings.CELERY_TASK_EAGER_PROPAGATES = True