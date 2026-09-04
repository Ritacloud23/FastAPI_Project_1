from fastapi import FastAPI, Query, Path, HTTPException

app = FastAPI()


vehicles = [
    {
        "id": 1,
        "make": "Toyota",
        "model": "Camry",
        "price": 20000000
    },
    {
        "id": 2,
        "make": "Honda",
        "model": "Accord",
        "price": 18000000
    },
    {
        "id": 3,
        "make": "Mercedes",
        "model": "C300",
        "price": 35000000
    },
    {
        "id": 4,
        "make": "Toyota",
        "model": "Corolla",
        "price": 15000000
    },
    {
        "id": 5,
        "make": "BMW",
        "model": "X5",
        "price": 40000000
    }
]


# Get one vehicle by ID
@app.get("/vehicles/{vehicle_id}")
def get_vehicle(
    vehicle_id: int = Path(gt=0)
):
    for vehicle in vehicles:
        if vehicle["id"] == vehicle_id:
            return vehicle

    raise HTTPException(
        status_code=404,
        detail="Vehicle not found"
    )


# Search and filter vehicles
@app.get("/vehicles")
def search_vehicles(
    make: str | None = Query(
        default=None,
        min_length=2,
        max_length=30
    ),
    model: str | None = Query(
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
    results = vehicles

    if make:
        results = [
            vehicle for vehicle in results
            if vehicle["make"].lower() == make.lower()
        ]

    if model:
        results = [
            vehicle for vehicle in results
            if vehicle["model"].lower() == model.lower()
        ]

    if min_price is not None:
        results = [
            vehicle for vehicle in results
            if vehicle["price"] >= min_price
        ]

    if max_price is not None:
        results = [
            vehicle for vehicle in results
            if vehicle["price"] <= max_price
        ]

    return results