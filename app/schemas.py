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

    class Config:
        from_attributes = True
