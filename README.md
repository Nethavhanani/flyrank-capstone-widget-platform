# FlyRank Capstone - Embeddable Widget Platform

A multi-tenant backend API for managing embeddable web widgets, schema validation, rate limiting, and real-time form submission processing.

---

## 🚀 Key Features

- **Multi-Tenant Architecture**: Built-in tenant isolation for tracking widgets and form submissions per account.
- **Dynamic Form Submissions API**: Validates, stores, and processes structured JSON form payloads.
- **Rate Limiting**: Built-in request throttle guards powered by `slowapi` to prevent submission abuse.
- **FastAPI & PostgreSQL**: High-performance asynchronous backend powered by SQLAlchemy ORM and PostgreSQL.
- **Docker Support**: Containerized environment configured via `docker-compose.yml`.

---

## 🛠️ Tech Stack

- **Framework**: Python 3.14 / FastAPI
- **Database**: PostgreSQL / SQLAlchemy ORM
- **Rate Limiting**: SlowAPI / Redis-ready
- **Server**: Uvicorn
- **Tooling**: Git, Docker, Pydantic

---

## 🏁 Quick Start

### 1. Prerequisites
- Python 3.10+
- PostgreSQL database
- Git

### 2. Environment Configuration
Clone the repository and copy `.env.example` to create your local `.env` configuration:

```bash
git clone [https://github.com/Nethavhanani/flyrank-capstone-widget-platform.git](https://github.com/Nethavhanani/flyrank-capstone-widget-platform.git)
cd flyrank-capstone-widget-platform
cp .env.example .env
