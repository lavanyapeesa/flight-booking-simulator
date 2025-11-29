from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime
import random

from app.database import SessionLocal
from app.schemas import FlightResponse
from app.models import Flight

router = APIRouter(prefix="/flights", tags=["Flights"])

# Correct get_db dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Get all flights
@router.get("/", response_model=List[FlightResponse])
def get_all_flights(db: Session = Depends(get_db)):
    return db.query(Flight).all()

#  Search flights (with filters + sorting + pagination)
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

    # Case-insensitive filtering
    if origin:
        query = query.filter(Flight.origin.ilike(f"%{origin}%"))
    if destination:
        query = query.filter(Flight.destination.ilike(f"%{destination}%"))

    # Airline filter
    if airline:
        query = query.filter(Flight.airline_name.ilike(f"%{airline}%"))

    # Class filter
    if travel_class:
        query = query.filter(Flight.travel_class.ilike(f"%{travel_class}%"))

    # Status filter
    if status:
        query = query.filter(Flight.status.ilike(f"%{status}%"))

    # Date filter (YYYY-MM-DD)
    if date:
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
            query = query.filter(func.date(Flight.departure) == parsed_date)
        except:
            raise HTTPException(
                status_code=400,
                detail="Invalid date format. Use YYYY-MM-DD"
            )

    # Sorting
    if sort_by:
        if sort_by == "price":
            query = query.order_by(Flight.base_fare.asc())
        elif sort_by == "duration":
            query = query.order_by(Flight.duration_minutes.asc())
        elif sort_by == "departure":
            query = query.order_by(Flight.departure.asc())
        else:
            raise HTTPException(
                status_code=400,
                detail="Invalid sort_by value. Use price/duration/departure"
            )

    # Pagination
    query = query.offset(offset).limit(limit)

    return query.all()


# Simulated Airline Schedule API (Option C)
@router.get("/external-feed")
def airline_feed_simulator():
    sample_airlines = ["IndiGo", "Air India", "Vistara", "SpiceJet"]
    sample_status = ["On-Time", "Delayed", "Cancelled"]

    return {
        "status": "success",
        "message": "Simulated airline schedule API",
        "data": {
            "airline": random.choice(sample_airlines),
            "status": random.choice(sample_status),
            "delay_minutes": random.choice([0, 10, 20, 45, 60])
        }
    }
