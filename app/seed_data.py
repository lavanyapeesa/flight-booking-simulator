from datetime import datetime
from .database import SessionLocal
from .models import Flight

def seed_flights():
    db = SessionLocal()

    flights = [
        Flight(
            flight_no="AI101",
            airline_name="Air India",
            origin="Delhi",
            destination="Mumbai",
            departure=datetime(2025, 3, 1, 10, 0),
            arrival=datetime(2025, 3, 1, 12, 0),
            duration_minutes=120,
            base_fare=8500,
            travel_class="Economy",
            total_seats=200,
            seats_available=180,
            status="Scheduled"
        ),
        Flight(
            flight_no="6E202",
            airline_name="IndiGo",
            origin="Bangalore",
            destination="Hyderabad",
            departure=datetime(2025, 3, 1, 15, 30),
            arrival=datetime(2025, 3, 1, 16, 40),
            duration_minutes=70,
            base_fare=4500,
            travel_class="Economy",
            total_seats=180,
            seats_available=160,
            status="Scheduled"
        ),
        Flight(
            flight_no="SG330",
            airline_name="SpiceJet",
            origin="Chennai",
            destination="Kolkata",
            departure=datetime(2025, 3, 1, 9, 45),
            arrival=datetime(2025, 3, 1, 12, 10),
            duration_minutes=145,
            base_fare=7400,
            travel_class="Economy",
            total_seats=160,
            seats_available=155,
            status="Scheduled"
        )
    ]

    db.add_all(flights)
    db.commit()
    db.close()

    print("Sample flight data inserted successfully.")

if __name__ == "__main__":
    seed_flights()
