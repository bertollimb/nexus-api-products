# Products API

REST API built with FastAPI for product management. The project implements full CRUD operations with PostgreSQL database persistence.

---

## About the Project

This API allows you to create, list, retrieve, and delete products. Data is persisted in a PostgreSQL database using SQLAlchemy async, making it a production-ready API structure built for learning and portfolio purposes.

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

---

## Project Structure

nexus-api-products/
├── api/
│   └── v1/
│       ├── api.py
│       └── endpoints/
│           └── product.py
├── alembic/
│   └── versions/
├── core/
│   ├── configs.py
│   ├── database.py
│   └── deps.py
├── models/
│   └── product_model.py
├── schemas/
│   └── product_schema.py
├── .env.example
├── .gitignore
├── alembic.ini
├── main.py
├── requirements.txt
└── LICENSE

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

pip install fastapi uvicorn pydantic sqlalchemy asyncpg alembic pydantic-settings python-dotenv

### 5. Configure environment variables

Copy the example file and fill in your database credentials:

cp .env.example .env

### 6. Run database migrations

alembic upgrade head

---

## Running the Project

python main.py

or

uvicorn main:app --reload

---

## API Endpoints

### GET /api/v1/products/
Returns a list of all products.

### GET /api/v1/products/{id}
Returns a product by its ID.

### POST /api/v1/products/
Creates a new product.

Example body:

{
  "name": "Product 1",
  "price": 10.5,
  "description": "Product description"
}

### DELETE /api/v1/products/{id}
Deletes a product by ID.

---

## Notes

- Data is persisted in a PostgreSQL database.
- Run migrations before starting the server for the first time.
- This project is intended for learning FastAPI, SQLAlchemy, and professional API structuring.

---

## Automatic Documentation

After starting the server:

- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

---

## Author

Project developed for backend study with Python and FastAPI.