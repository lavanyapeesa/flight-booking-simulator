from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime
import random

from app.database import SessionLocal
from app.schemas import FlightResponse
from app.models import Flight

from app.utils.pricing_engine import calculate_dynamic_price
from app.utils.demand_simulator import get_demand_factor


router = APIRouter(prefix="/flights", tags=["Flights"])


# DB DEPENDENCY

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET ALL FLIGHTS (with dynamic pricing)

@router.get("/", response_model=List[FlightResponse])
def get_all_flights(db: Session = Depends(get_db)):
    flights = db.query(Flight).all()

    for f in flights:
        demand = get_demand_factor()

        f.base_fare = calculate_dynamic_price(
            base_fare=float(f.base_fare),
            seats_available=f.seats_available,
            total_seats=f.total_seats,
            departure_time=f.departure,
            demand_factor=demand
        )
    return flights

# SEARCH FLIGHTS (filters + sort + pagination + dynamic price)

   @router.get("/search", response_model=List[FlightResponse])
def search_flights(
    origin: Optional[str] = None,
    destination: Optional[str] = None,
    date: Optional[str] = None,
    airline: Optional[str] = None,
    travel_class: Optional[str] = None,
    status: Optional[str] = None,
    sort_by: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db)
):

    query = db.query(Flight)

    # ----- FILTERS -----
    if origin:
        query = query.filter(Flight.origin.ilike(f"%{origin}%"))
    if destination:
        query = query.filter(Flight.destination.ilike(f"%{destination}%"))
    if airline:
        query = query.filter(Flight.airline_name.ilike(f"%{airline}%"))
    if travel_class:
        query = query.filter(Flight.travel_class.ilike(f"%{travel_class}%"))
    if status:
        query = query.filter(Flight.status.ilike(f"%{status}%"))

    if date:
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
            query = query.filter(func.date(Flight.departure) == parsed_date)
        except:
            raise HTTPException(status_code=400, detail="Invalid date format")

    # ----- SORTING -----
    if sort_by == "price":
        query = query.order_by(Flight.base_fare.asc())
    elif sort_by == "duration":
        query = query.order_by(Flight.duration_minutes.asc())
    elif sort_by == "departure":
        query = query.order_by(Flight.departure.asc())
    elif sort_by:
        raise HTTPException(status_code=400, detail="Invalid sort option")

    # ----- PAGINATION -----
    flights = query.offset(offset).limit(limit).all()

    # ----- APPLY DYNAMIC PRICING -----
    for f in flights:
        demand = get_demand_factor()

        f.base_fare = calculate_dynamic_price(
            base_fare=float(f.base_fare),
            seats_available=f.seats_available,
            total_seats=f.total_seats,
            departure_time=f.departure,
            demand_factor=demand
        )

    return flights


# SIMULATED EXTERNAL AIRLINE API
@router.get("/external-feed")
def airline_feed_simulator():
    sample_airlines = ["IndiGo", "Air India", "Vistara", "SpiceJet"]
    sample_status = ["On-Time", "Delayed", "Cancelled"]

    return {
        "status": "success",
        "data": {
            "airline": random.choice(sample_airlines),
            "status": random.choice(sample_status),
            "delay_minutes": random.choice([0, 5, 10, 30, 60])
        }
    }
