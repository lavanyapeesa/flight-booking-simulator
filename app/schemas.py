from pydantic import BaseModel
from datetime import datetime

class FlightBase(BaseModel):
    flight_no: str
    airline_name: str
    origin: str
    destination: str
    departure: datetime
    arrival: datetime
    duration_minutes: int
    base_fare: float
    travel_class: str
    total_seats: int
    seats_available: int
    status: str

class FlightResponse(FlightBase):
    id: int
    created_at: datetime
    updated_at: datetime

# -------------------------------
# Booking Schemas
# -------------------------------

class BookingCreate(BaseModel):
    flight_id: int
    passenger_name: str
    passenger_contact: str
    seat_number: int


class BookingResponse(BaseModel):
    id: int
    flight_id: int
    passenger_name: str
    passenger_contact: str
    seat_number: int
    price_paid: float
    booking_status: str
    pnr: str
    created_at: datetime

    class Config:
        from_attributes = True
