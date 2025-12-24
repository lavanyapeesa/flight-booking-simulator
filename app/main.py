from fastapi import FastAPI
from app.routers import flights, bookings

app = FastAPI(title="Flight Booking Simulator")

@app.get("/")
def root():
    return {"message": "Flight Booking Simulator API is running"}

# Include routers
app.include_router(flights.router)
app.include_router(bookings.router)
