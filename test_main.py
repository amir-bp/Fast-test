from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app, inventory

client = TestClient(app)


# def setup_function():
#     inventory.clear()

def test_read_inventory():
    response = client.get("/get-item/2")
    assert response.status_code == 200
    assert response.json() == {**inventory["2"]}


def test_read_all_items():
    response = client.get("/get-all-items")
    assert response.status_code == 200
    assert response.json() == {**inventory}


def test_create_item():
    response = client.post("/create-item/3", json={"item_id": 3, "name": "water", "price": 1.99, "brand": "dairy"})
    assert response.status_code == 200
    assert response.json() == {**inventory[3]}
