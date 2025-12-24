from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import uuid

from app.database import SessionLocal
from app.models import Flight, Booking
from app.schemas import BookingCreate, BookingResponse

router = APIRouter(prefix="/bookings", tags=["Bookings"])


# ---------------------------------------------------------
# Database dependency
# ---------------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------------------------------------
# 📌 Create Booking
# ---------------------------------------------------------
@router.post("/", response_model=BookingResponse)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):

    # 1️⃣ Check flight exists
    flight = db.query(Flight).filter(Flight.id == booking.flight_id).first()
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")

    # 2️⃣ Check seats available
    if flight.seats_available <= 0:
        raise HTTPException(status_code=400, detail="No seats available")

    # 3️⃣ Prevent double booking of same seat
    seat_taken = db.query(Booking).filter(
        Booking.flight_id == booking.flight_id,
        Booking.seat_number == booking.seat_number,
        Booking.booking_status == "CONFIRMED"
    ).first()

    if seat_taken:
        raise HTTPException(
            status_code=400,
            detail="Seat already booked"
        )

    # 4️⃣ Reduce seat count
    flight.seats_available -= 1

    # 5️⃣ Calculate final price
    final_price = float(flight.base_fare)

    # 6️⃣ Generate PNR
    pnr_code = "PNR-" + uuid.uuid4().hex[:8].upper()

    # 7️⃣ Create booking entry
    new_booking = Booking(
        flight_id=booking.flight_id,
        passenger_name=booking.passenger_name,
        passenger_contact=booking.passenger_contact,
        seat_number=booking.seat_number,
        price_paid=final_price,
        booking_status="CONFIRMED",
        pnr=pnr_code,
        created_at=datetime.utcnow()
    )

    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    return new_booking


# ---------------------------------------------------------
# ❌ Cancel Booking
# ---------------------------------------------------------
@router.delete("/{pnr}")
def cancel_booking(pnr: str, db: Session = Depends(get_db)):

    booking = db.query(Booking).filter(Booking.pnr == pnr).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    if booking.booking_status == "CANCELLED":
        return {"message": "Booking already cancelled"}

    # Restore seat availability
    flight = db.query(Flight).filter(Flight.id == booking.flight_id).first()
    if flight:
        flight.seats_available += 1

    booking.booking_status = "CANCELLED"
    db.commit()

    return {
        "message": "Booking cancelled successfully",
        "pnr": booking.pnr,
        "status": booking.booking_status
    }


# ---------------------------------------------------------
# 📜 Booking History
# ---------------------------------------------------------
@router.get("/history", response_model=list[BookingResponse])
def booking_history(
    passenger_contact: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Booking)

    if passenger_contact:
        query = query.filter(
            Booking.passenger_contact == passenger_contact
        )

    bookings = query.all()

    if not bookings:
        raise HTTPException(
            status_code=404,
            detail="No bookings found"
        )

    return bookings

