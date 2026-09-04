from fastapi import FastAPI, Query

app = FastAPI()


products = [
    {
        "name": "iPhone 15",
        "category": "electronics",
        "price": 800000
    },
    {
        "name": "Samsung Galaxy S24",
        "category": "electronics",
        "price": 750000
    },
    {
        "name": "Nike Air Max",
        "category": "shoes",
        "price": 150000
    },
    {
        "name": "Adidas Superstar",
        "category": "shoes",
        "price": 120000
    },
    {
        "name": "Dell Laptop",
        "category": "computers",
        "price": 650000
    },
]


@app.get("/products")
def search_products(
    name: str | None = Query(
        default=None,
        min_length=2,
        max_length=50
    ),
    category: str | None = Query(
        default=None,
        min_length=2,
        max_length=30
    ),
    min_price: float | None = Query(
        default=None,
        ge=0
    ),
    max_price: float | None = Query(
        default=None,
        ge=0
    )
):
    results = products

    if name:
        results = [
            product for product in results
            if name.lower() in product["name"].lower()
        ]

    if category:
        results = [
            product for product in results
            if category.lower() == product["category"].lower()
        ]

    if min_price is not None:
        results = [
            product for product in results
            if product["price"] >= min_price
        ]

    if max_price is not None:
        results = [
            product for product in results
            if product["price"] <= max_price
        ]

    return results