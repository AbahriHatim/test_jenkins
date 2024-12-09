from fastapi.testclient import TestClient
from main import app, DATA_FILE
import os
import json

client = TestClient(app)

# Helper to reset the data file before each test
def reset_data_file():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)

def test_create_client():
    reset_data_file()
    response = client.post("/clients/", json={
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"
    assert data["phone"] == "1234567890"

def test_read_client():
    reset_data_file()
    # Create a client first
    client.post("/clients/", json={
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890"
    })
    response = client.get("/clients/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "John Doe"

def test_update_client():
    reset_data_file()
    # Create a client first
    client.post("/clients/", json={
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890"
    })
    response = client.patch("/clients/1", json={"name": "Jane Doe"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jane Doe"

def test_delete_client():
    reset_data_file()
    # Create a client first
    client.post("/clients/", json={
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890"
    })
    response = client.delete("/clients/1")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Client deleted"
    # Ensure the client is no longer available
    response = client.get("/clients/1")
    assert response.status_code == 404
