from fastapi import FastAPI

from models import EventBooking, BookingConfirmation

app = FastAPI()


@app.post("/bookings/", response_model=BookingConfirmation)
async def book_event(booking: EventBooking):
    return BookingConfirmation(
        message="Booking confirmed!",
        attendee_name=booking.attendee.name,
        event_name=booking.event.name,
        event_date=booking.event.date,
        location=booking.event.location,
        ticket_type=booking.ticket_type,
    )