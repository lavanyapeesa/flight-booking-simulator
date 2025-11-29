from fastapi import FastAPI
from .routers import flights

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Flight Booking Simulator API is running"}

app.include_router(flights.router)