from fastapi import FastAPI, Path

app = FastAPI()



inventory = {
        "1": {
            "name": "egg",
            "price": 3.99,
            "brand": "Regular"
        },
        "2": {
            "name": "milk",
            "price": 7.99,
            "brand": "Imported"

        }
    }



# inventory = {
#         1: {
#             "name": "egg",
#             "price": 3.99,
#             "brand": "Regular"
#         },
#         2: {
#             "name": "milk",
#             "price": 7.99,
#             "brand": "Imported"

#         },
#         3: {
#             "name": "bread",
#             "price": 2.99,
#             "brand": "Local"
#         },
#     }


@app.get("/get-all-items")
def get_all_items():
    return inventory



@app.get("/get-item/{item_id}")
def get_item(item_id: str = Path(description = "The ID of the item you'd like to view.")):
    return inventory[item_id]





@app.get("/get-by-name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {'Data': 'Not Found'}


@app.post("/create-item/{item_id}")
def create_item(item_id: int, name: str, price: float, brand: str):

    inventory[item_id] = {"name": name, "price": price, "brand": brand}
    return inventory[item_id]












# def get_item(item_id: int = Path(None, description = "The ID of the item you'd like to view.", le=1)):










# from fastapi import FastAPI, Query
#
# app = FastAPI()
#
# inventory = {
#     1: {
#         "name": "Milk",
#         "price": 3.99,
#         "branch": "Regular"
#     }
# }
#
# @app.get("/get-item/")
# def get_item(item_id: int = Query(None, description="The ID of the item you want")):
#     if item_id is not None:
#         return inventory.get(item_id, {"error": "Item not found"})
#     else:
#         return {"error": "Item ID is required"}
