from datetime import date
from pydantic import BaseModel, Field, EmailStr


class FlightDetails(BaseModel):
    origin: str = Field(min_length=3, max_length=50)
    destination: str = Field(min_length=3, max_length=50)
    flight_date: date
    flight_number: int = Field(
        gt=0,
        description="Flight number must be positive"
    )

class ContactDetails(BaseModel):
    email: EmailStr
    phone: str = Field(
        min_length=10,
        max_length=15
    )

class PassengerInformation(BaseModel):
    name: str = Field(
        min_length=5,
        max_length=15,
        description="Passenger full name"
    )
    age: int = Field(
        ge=1,
        le=120,
        description="Passenger age"
    )
    contact: ContactDetails
    flight: FlightDetails