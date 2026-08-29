# Products API

A REST API for product management, built with FastAPI as a backend study project — full CRUD, async database access, and JWT authentication implemented from scratch (not scaffolded from a template).

**Live API docs:** https://nexus-api-products.onrender.com/docs

## About the project

This API allows creating, listing, retrieving, updating, and deleting products, with data persisted in PostgreSQL through fully async SQLAlchemy. It also includes a complete user system with JWT authentication, protecting write/sensitive endpoints from unauthorized access. The project was built to practice professional API structuring (layered architecture, migrations, automated testing) rather than as a one-off script.

## Tech stack

- **Python 3.12** / **FastAPI**
- **PostgreSQL** (Supabase) with **SQLAlchemy** (fully async)
- **Alembic** — database migrations
- **Pydantic** / **Pydantic Settings**
- **JWT** authentication (python-jose, passlib, python-multipart)
- **pytest** / **pytest-asyncio** / **httpx** — automated test suite, running against an isolated SQLite database
- **Docker** — containerized deployment
- Deployed on **Render**

## Project structure

```
nexus-api-products/
├── api/
│   └── v1/
│       ├── api.py
│       └── endpoints/
│           ├── product.py
│           └── user.py
├── alembic/
│   └── versions/
├── core/
│   ├── configs.py
│   ├── database.py
│   └── security.py
├── models/
│   ├── product_model.py
│   └── user_model.py
├── schemas/
│   ├── product_schema.py
│   └── user_schema.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_products.py
│   └── test_users.py
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── LICENSE
├── main.py
├── pytest.ini
└── requirements.txt
```

## Getting started

### Prerequisites
- Python 3.12+
- A PostgreSQL database (this project uses [Supabase](https://supabase.com))

### Local setup

```bash
git clone https://github.com/bertollimb/nexus-api-products
cd nexus-api-products
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Copy the example file and fill in your own credentials:

```bash
cp .env.example .env
```

Apply migrations and run:

```bash
alembic upgrade head
uvicorn main:app --reload
```

API available at `http://localhost:8000/docs` (Swagger) or `http://localhost:8000/redoc`.

### Running with Docker

```bash
docker build -t nexus-api-products .
docker run --rm -p 8000:8000 --env-file .env nexus-api-products
```

### Running the test suite

```bash
pytest -v
```

Tests run against an isolated SQLite database and never touch the PostgreSQL data used in development or production.

## Authentication

This API uses JWT Bearer token authentication:

1. Register via `POST /api/v1/users/signup`
2. Log in via `POST /api/v1/users/login` to receive an access token
3. Send the token on protected endpoints:
   ```
   Authorization: Bearer <your_token>
   ```

Protected endpoints return `401 Unauthorized` when accessed without a valid token.

## API endpoints

**Users**
| Method | Path | Description |
|---|---|---|
| POST | `/api/v1/users/signup` | Register a new user |
| POST | `/api/v1/users/login` | Log in and receive a JWT token |
| GET | `/api/v1/users/logged` | Get the current authenticated user (protected) |
| GET | `/api/v1/users/` | List all users (protected) |
| GET | `/api/v1/users/{id}` | Get user by ID |
| PUT | `/api/v1/users/{id}` | Update user (protected) |
| DELETE | `/api/v1/users/{id}` | Delete user (protected) |

**Products**
| Method | Path | Description |
|---|---|---|
| GET | `/api/v1/products/` | List all products |
| GET | `/api/v1/products/{id}` | Get product by ID |
| POST | `/api/v1/products/` | Create a new product |
| PUT | `/api/v1/products/{id}` | Update product (protected) |
| DELETE | `/api/v1/products/{id}` | Delete product |

Example `POST /api/v1/products/` body:
```json
{
  "name": "Product 1",
  "price": 10.5,
  "description": "Product description"
}
```

## Deployment

- **API**: Docker container on [Render](https://render.com) (Frankfurt region), built directly from the repository's `Dockerfile`
- **Database**: [Supabase](https://supabase.com) — managed PostgreSQL (Frankfurt region)

Environment variables (`DB_URL`, `JWT_SECRET`, and optionally `ALGORITHM`, `ACCESS_TOKEN_EXPIRE_MINUTES`, `REFRESH_TOKEN_EXPIRE_DAYS`) are configured directly on Render and are never baked into the Docker image — `.dockerignore` explicitly excludes `.env`, `venv/`, and other files that shouldn't ship inside the container.

## Notes

- Migrations must be applied before starting the server for the first time.
- Tests use an isolated in-memory SQLite database, kept separate from the PostgreSQL data used in development and production.
- Built for learning FastAPI, async SQLAlchemy, and professional-grade API structuring.