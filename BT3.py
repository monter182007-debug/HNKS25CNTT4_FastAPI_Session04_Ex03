from fastapi import FastAPI
from typing import Optional

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse", "price": 200000},
    {"id": 3, "name": "Keyboard", "price": 500000},
    {"id": 4, "name": "Monitor", "price": 3000000}
]

@app.get("/products")
def search_products(keyword: Optional[str] = None, max_price: Optional[float] = None):
    
    if max_price is not None and max_price < 0:
        return {"detail": "max_price không được âm"}
    
    result = products

    if keyword is not None:
        result = [p for p in result if keyword.lower() in p["name"].lower()]

    if max_price is not None:
        result = [p for p in result if p["price"] <= max_price]
    return result