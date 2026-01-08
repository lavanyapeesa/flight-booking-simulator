from fastapi import FastAPI
from app.routers import flights, bookings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Flight Booking Simulator")

@app.get("/")
def root():
    return {"message": "Flight Booking Simulator API is running"}

# Include routers
app.include_router(flights.router)
app.include_router(bookings.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

