# Design Document: FlyRank Widget & Lead-Capture Platform

## 1. Data Model
- **Tenants**: Represents widget owners (id, email, created_at).
- **Widgets**: Stores widget configurations, form settings, and tenant ownership (id, tenant_id, title, widget_type, settings, created_at).
- **Submissions**: Stores incoming public lead submissions enriched with IP and geo-location data (id, widget_id, payload, ip_address, geo_data, created_at).

## 2. API Architecture & Request Paths
- **Admin Path (Authenticated)**: CRUD operations on `/api/v1/widgets` for owners.
- **Delivery Path (Public & Cached)**: GET `/api/v1/widgets/:id/config` serving config JSON with HTTP Cache-Control headers.
- **Submission Path (Public CORS & Hardened)**: POST `/api/v1/submissions` accepting cross-origin form submissions with boundary validation, rate limiting, honeypot check, and geo-enrichment fallback.

## 3. Explicit Non-Goals
- No full custom drag-and-drop form builder frontend.
- No real CDN distribution (hosted locally / Docker).
