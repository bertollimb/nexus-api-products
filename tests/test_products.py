async def test_create_product(client):
    response = await client.post("/api/v1/products/", json={
        "name": "Notebook",
        "price": 2500.0,
        "description": "Notebook dell"
    })
    assert response.status_code == 201
    assert response.json()["name"] == "Notebook"
    assert response.json()["price"] == 2500.0
    assert response.json()["description"] == "Notebook dell"

async def test_get_products(client):
    response = await client.get("/api/v1/products/")
    assert response.status_code == 200

async def test_get_product_by_id(client):
    response = await client.get("/api/v1/products/1")
    assert response.status_code == 200

async def test_get_product_not_found(client):
    response = await client.get("/api/v1/products/10")
    assert response.status_code == 404

async def test_update_product_without_token(client):
    response = await client.put("/api/v1/products/1", json={
        "name": "Smartphone",
        "price": 1200.0,
        "description": "Samsung A20"
    })
    assert response.status_code == 401

async def test_update_product_with_token(client):
    await client.post("/api/v1/users/signup", json={
        "name": "Bruna",
        "lastname": "Bertolli",
        "email": "bruna@test.com",
        "password": "test4321",
        "is_admin": False
    })

    login_response = await client.post("/api/v1/users/login", data={
        "username": "bruna@test.com",
        "password": "test4321"
    })
    token = login_response.json()["access_token"]

    response = await client.put("/api/v1/products/1", json={
        "name": "Smartphone",
        "price": 1200.0,
        "description": "Samsung A20"
    }, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 202
    assert response.json()["name"] == "Smartphone"
    assert response.json()["price"] == 1200.0
    assert response.json()["description"] == "Samsung A20"


async def test_delete_product(client):
    response = await client.delete("/api/v1/products/1")
    assert response.status_code == 204