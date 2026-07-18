# Products API

REST API built with FastAPI for product management. The project implements full CRUD operations with PostgreSQL database persistence, JWT authentication, and automated tests.

---

## About the Project

This API allows you to create, list, retrieve, update, and delete products. Data is persisted in a PostgreSQL database using SQLAlchemy async. The API includes a complete user management system with JWT authentication, protecting sensitive endpoints from unauthorized access. The project includes an automated test suite covering the main API flows.

---

## Technologies Used

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- PostgreSQL
- SQLAlchemy (async)
- Alembic
- Pydantic Settings
- python-jose
- passlib
- python-multipart
- pytest
- pytest-asyncio
- httpx

---

## Project Structure
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
│   ├── auth.py
│   ├── configs.py
│   ├── database.py
│   ├── deps.py
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
├── .env.example
├── .gitignore
├── alembic.ini
├── pytest.ini
├── main.py
├── requirements.txt
└── LICENSE
```
---

## Prerequisites

- Python 3.10+
- PostgreSQL running locally

---

## Installation

### 1. Clone the repository

git clone https://github.com/bertollimb/nexus-api-products
cd nexus-api-products

### 2. Create a virtual environment

python -m venv venv

### 3. Activate the virtual environment

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

### 4. Install dependencies

pip install fastapi uvicorn pydantic sqlalchemy asyncpg alembic pydantic-settings python-dotenv python-jose passlib python-multipart pytest pytest-asyncio httpx aiosqlite

### 5. Configure environment variables

Copy the example file and fill in your credentials:

cp .env.example .env

### 6. Run database migrations

alembic upgrade head

---

## Running the Project

python main.py

or

uvicorn main:app --reload

---

## Running Tests

pytest tests/ -v

Tests use an isolated SQLite database and do not affect your PostgreSQL data.

---

## Authentication

This API uses JWT Bearer token authentication.

1. Register a new user via POST /api/v1/users/signup
2. Login via POST /api/v1/users/login to receive your access token
3. Use the token in the Authorization header for protected endpoints:

Authorization: Bearer <your_token>

Protected endpoints return 401 Unauthorized when accessed without a valid token.

---

## API Endpoints

### Users

POST /api/v1/users/signup — register a new user
POST /api/v1/users/login — login and receive JWT token
GET /api/v1/users/logged — get current authenticated user (protected)
GET /api/v1/users/ — list all users (protected)
GET /api/v1/users/{id} — get user by ID
PUT /api/v1/users/{id} — update user (protected)
DELETE /api/v1/users/{id} — delete user (protected)

### Products

GET /api/v1/products/ — list all products
GET /api/v1/products/{id} — get product by ID
POST /api/v1/products/ — create new product

Example body:

{
  "name": "Product 1",
  "price": 10.5,
  "description": "Product description"
}

PUT /api/v1/products/{id} — update product (protected)
DELETE /api/v1/products/{id} — delete product

---

## Notes

- Data is persisted in a PostgreSQL database.
- Run migrations before starting the server for the first time.
- Tests use an isolated SQLite in-memory database.
- This project is intended for learning FastAPI, SQLAlchemy, and professional API structuring.

---

## Automatic Documentation

After starting the server:

- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

---

## Author

Project developed for backend study with Python and FastAPI.