# Multi-Tenant B2B Platform
Engineered a multi-tenant architecture using Django and PostgreSQL, ensuring secure data isolation between corporate clients.
- Optimized performance by offloading heavy tasks (Invoicing/Emails) to Celery background workers, reducing API latency by 70%.
- Built production-ready code with Docker containerization and achieved 90% test coverage using Pytest to ensure system reliability.

## What I built
I developed a secure, multi-tenant application architecture that isolates tenant data while sharing common business logic. The system is designed for B2B use cases and supports:

- Tenant-aware routing via custom middleware, resolving tenant context from subdomains and injecting it into every request.
- Strong row-level isolation using a tenant-aware Django manager so queries only return data for the active tenant.
- Improved performance using ORM optimization techniques such as `select_related` and `prefetch_related` to eliminate N+1 query patterns.
- Asynchronous processing with Celery and Redis to handle invoice workflows and notifications without blocking user-facing API calls.
- Docker-based local development and deployment for environment consistency.

## Why it matters
This project demonstrates my ability to build backend systems that combine security, scalability, and maintainability for enterprise SaaS products:

- Designed to protect tenant boundaries and prevent data leaks.
- Implemented reusable architecture patterns for multi-tenant Django applications.
- Delivered clean API-driven services with reliable asynchronous task handling.

## Technologies
- Python 3.12
- Django 5.0
- Django REST Framework
- PostgreSQL 15
- Redis 7
- Celery 5.3
- Docker / Docker Compose
- Pytest / pytest-cov

## Highlights
- Built a custom tenant middleware layer for thread-safe tenant context management.
- Created reusable tenant-aware model behavior via `TenantAwareModel`.
- Designed REST API endpoints with DRF viewsets for invoices.
- Added end-to-end tests for tenant isolation and async task execution.

## Run locally
```bash
docker compose up
docker compose up -d db redis
docker compose run --rm web pytest
```

## Project structure
- `core/` — project settings, URL routing, and app configuration
- `tenants/` — tenant routing, middleware, models, and auth views
- `billing/` — invoice models, serializers, API endpoints, and Celery tasks
- `templates/` — frontend UI templates for tenant dashboard and login

This repository represents hands-on experience building scalable backend systems for B2B SaaS products.
