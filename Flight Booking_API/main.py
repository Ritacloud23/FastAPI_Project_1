from fastapi import FastAPI

from models import PassengerInformation

app = FastAPI()


@app.post("/Bookings/")
async def booking(passenger: PassengerInformation):
    return passenger