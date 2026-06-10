# Products API

Simple REST API built with FastAPI for product management. The project implements basic CRUD operations using in-memory storage.

---

## About the Project

This API allows you to create, list, retrieve, and delete products. Data is temporarily stored in memory (Python dictionary), making it ideal for learning purposes and API prototyping with FastAPI.

---

##  Technologies Used

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

---

##  Project Structure

```
```
fastapi-products-api/
├── api/
│   └── v1/
│       ├── api.py
│       └── endpoints/
│           ├── product.py
├── schemas/
│   ├── product_schema.py
│
├── .gitignore
├── main.py
├── requirements.txt
└── LICENSE
```

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/bertollimb/nexus-api-products
cd nexus-api-products
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

---

##  Running the Project

```bash
python main.py
```

or

```bash
uvicorn main:app --reload
```

---

##  API Endpoints

### GET /products/
Returns a list of all products.

### GET /products/{id}
Returns a product by its ID.

### POST /products/
Creates a new product.

Example body:

```json
{
  "name": "Product 1",
  "price": 10.5,
  "description": "Product description"
}
```

### DELETE /products/{id}
Deletes a product by ID.

---

##  Notes

- Data is stored in memory (no database).
- All data is lost when the server restarts.
- This project is intended for learning FastAPI and API structuring.

---

##  Automatic Documentation

After starting the server:

- Swagger UI: http://localhost:8000/docs  
- Redoc: http://localhost:8000/redoc  

---

## Author

Project developed for backend study with Python and FastAPI.