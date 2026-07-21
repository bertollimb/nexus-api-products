USER_DATA = {
    "name": "Matheus",
    "lastname": "Anastácio",
    "email": "matheus@test.com",
    "password": "test1234",
    "is_adimn": False
}

async def test_signup_success(client):
    response = await client.post("/api/v1/users/signup", json=USER_DATA)
    assert response.status_code == 201
    assert response.json()["email"] == USER_DATA["email"]

async def test_signup_duplicate_email(client):
    response = await client.post("/api/v1/users/signup", json=USER_DATA)
    assert response.status_code == 406

async def test_login_success(client):
    response = await client.post("/api/v1/users/login", data={
        "username": USER_DATA["email"],
        "password": USER_DATA["password"]
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

async def test_login_wrong_password(client):
    response = await client.post("/api/v1/users/login", data={
        "username": USER_DATA["email"],
        "password": "incorrect password"
    })
    assert response.status_code == 400