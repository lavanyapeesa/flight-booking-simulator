from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy import Boolean
from datetime import datetime
from .database import Base

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    flight_no = Column(String(10), unique=True, nullable=False)
    airline_name = Column(String(50), nullable=False)

    origin = Column(String(50), nullable=False)
    destination = Column(String(50), nullable=False)

    departure = Column(DateTime, nullable=False)
    arrival = Column(DateTime, nullable=False)
    duration_minutes = Column(Integer, nullable=False)

    base_fare = Column(Numeric(10, 2), nullable=False)

    travel_class = Column(String(20), default="Economy")

    total_seats = Column(Integer, nullable=False)
    seats_available = Column(Integer, nullable=False)

    status = Column(String(20), default="Scheduled")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
