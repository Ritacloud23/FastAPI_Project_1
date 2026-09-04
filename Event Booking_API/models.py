from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, EmailStr, field_validator


class TicketTypeEnum(str, Enum):
    standard = "standard"
    vip = "vip"
    early_bird = "early_bird"


class AttendeeInformation(BaseModel):
    name: str = Field(min_length=5, max_length=25, description="Attendee full name")
    email: EmailStr
    age: int = Field(ge=18, le=85, description="Age must be between 18 and 85")


class EventDetails(BaseModel):
    name: str = Field(min_length=5, max_length=25, description="Event name")
    date: datetime = Field(description="Event date/time, must be in the future")
    location: str = Field(min_length=5, max_length=25)


class EventBooking(BaseModel):
    attendee: AttendeeInformation
    event: EventDetails
    ticket_type: TicketTypeEnum


class BookingConfirmation(BaseModel):
    message: str
    attendee_name: str
    event_name: str
    event_date: datetime
    location: str
    ticket_type: TicketTypeEnum