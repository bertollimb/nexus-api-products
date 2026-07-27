async def test_create_product(client):
    response = await client.post("/api/v1/products/", json={
        "name": "Notebook",
        "price": 2500.0,
        "description": "Notebook dell"
        }
    )

    data = response.json()

    assert response.status_code == 201
    assert data["name"] == "Notebook"
    assert data["price"] == 2500.0
    assert data["description"] == "Notebook dell"

async def test_get_products(client, created_product):
    response = await client.get("/api/v1/products/")

    data = response.json()

    assert response.status_code == 200
    assert len(data) == 1

async def test_get_product_by_id(client, created_product):
    response = await client.get(f"/api/v1/products/{created_product['id']}")

    data = response.json()

    assert response.status_code == 200
    assert data["id"] == created_product["id"]

async def test_get_product_not_found(client, created_product):
    response = await client.get("/api/v1/products/999")
    assert response.status_code == 404

async def test_update_product_without_token(client, created_product):
    response = await client.put(f"/api/v1/products/{created_product['id']}", json={
        "name": "Smartphone",
        "price": 1200.0,
        "description": "Samsung A20"
        }
    )

    assert response.status_code == 401

async def test_update_product_with_token(client,auth_token, created_product):
    response = await client.put(f"/api/v1/products/{created_product['id']}", json={
        "name": "Smartphone",
        "price": 1200.0,
        "description": "Samsung A20"
    }, headers={"Authorization": f"Bearer {auth_token}"})

    data = response.json()

    assert response.status_code == 202
    assert data["name"] == "Smartphone"
    assert data["price"] == 1200.0
    assert data["description"] == "Samsung A20"


async def test_delete_product(client, auth_token, created_product):
    response = await client.delete(f"/api/v1/products/{created_product['id']}",
                                   headers={"Authorization": f"Bearer {auth_token}"})
    
    assert response.status_code == 204

