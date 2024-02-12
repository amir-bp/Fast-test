import pytest
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


''' Farzam bhai can you please help me with this code. yahan par men name likh kr data lena chah rha hu, route men data
    show horha hai, lekin test fail horha hai for some reason.
 '''
def test_read_by_name():
    response = client.get("/get-by-name")
    item_id = inventory["1"]['name']
    assert response.status_code == 200
    assert response.json() == {item_id}
    




# @pytest.mark.parametrized("name, expected_status_code" [
#     {
#         "egg", 200
#     }
# ])
# def test_read_by_name(name, expected_status_code):
#     response = client.get(f"/get-by-name?name={name}")
#     # item_name = inventory[item_id]['name']
#     assert response.status_code == expected_status_code
#     assert response.json() == {"name": "egg", "price": 3.99, "brand": "Regular"}


def test_create_item():
    item_data = {
        "name": "milk",
        "price": 7.99,
        "brand": "Imported"
    }
    response = client.post("/create-item", json=item_data)
    if response.status_code == 200:
        print(response.json())
    assert response.status_code == 200
    assert response.json() == {"name": "milk", "price": 7.99, "brand": "Imported"}



