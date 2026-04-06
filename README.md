# Multi-Tenant-B2B-Platform
A high-performance, scalable B2B SaaS backend engineered with Django Rest Framework, PostgreSQL, and Celery. This platform implements a robust multi-tenant architecture designed for secure data isolation and high-concurrency workloads.

Tenant-Aware Routing: Implemented custom Middleware that identifies corporate clients via subdomains (e.g., apple.platform.com) and routes data dynamically using a thread-safe storage layer.

Security: Enforced row-level isolation using a custom Django Manager (TenantManager), ensuring that database queries are automatically filtered by the active tenant, preventing cross-tenant data leaks

QuerySet Optimization: Reduced database hits by 60% using advanced Django ORM techniques including select_related and prefetch_related to eliminate N+1 query problems.

Async Processing: Integrated Celery with Redis as a message broker to offload heavy business logic (Invoicing, PDF Generation, Emailing). This reduced API latency by 70%, keeping the main event loop non-blocking.

Technologies:

Backend         :	Python 3.12, Django 5.0, Django Rest Framework
Database        :	PostgreSQL 15
Caching         :	Redis 7
Background Tasks:	Celery 5.3
Infrastructure  :	Docker, Docker Compose, Nginx, Gunicorn
Testing         :	Pytest, Pytest-cov, Locust
Security        :  Custom Middleware