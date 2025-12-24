from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
import uuid


# -------------------------
# FLIGHT TABLE
# -------------------------
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

    # Relationship
    bookings = relationship("Booking", back_populates="flight")


# -------------------------
# BOOKING TABLE (Milestone 3)
# -------------------------
class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    flight_id = Column(Integer, ForeignKey("flights.id"), nullable=False)

    passenger_name = Column(String(100), nullable=False)
    passenger_contact = Column(String(20), nullable=False)

    seat_number = Column(Integer, nullable=False)
    price_paid = Column(Numeric(10, 2), nullable=False)

    booking_status = Column(String(20), default="CONFIRMED")
    pnr = Column(String(20), unique=True, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    flight = relationship("Flight")
