from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app, inventory

client = TestClient(app)


def setup_function():
    inventory.clear()
    inventory.update({
        1: {
            "name": "Milk",
            "price": 3.99,
            "brand": "Regular"
        },
        2: {
            "name": "Bread",
            "price": 2.99,
            "brand": "Local"
        }
    })





