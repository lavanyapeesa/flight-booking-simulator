from datetime import datetime

def calculate_dynamic_price(base_fare, seats_available, total_seats, departure_time, demand_factor):
    """
    Dynamic Price = base_fare + seat_factor + time_factor + demand_factor_adjustment
    """

    # -------------------------
    # Seat Availability Factor
    # -------------------------
    seats_left_percentage = seats_available / total_seats

    if seats_left_percentage > 0.7:
        seat_factor = 0
    elif seats_left_percentage > 0.4:
        seat_factor = base_fare * 0.10
    elif seats_left_percentage > 0.2:
        seat_factor = base_fare * 0.20
    else:
        seat_factor = base_fare * 0.40  # very low seats → very high price

    # -------------------------
    # Time to Departure Factor
    # -------------------------
    # closer flight → higher prices
    now = datetime.utcnow()
    hours_left = (departure_time - now).total_seconds() / 3600

    if hours_left < 6:
        time_factor = base_fare * 0.50
    elif hours_left < 24:
        time_factor = base_fare * 0.30
    elif hours_left < 72:
        time_factor = base_fare * 0.10
    else:
        time_factor = 0

    # -------------------------
    #  Demand Factor (from simulator)
    # -------------------------
    if demand_factor == "HIGH":
        demand_adjustment = base_fare * 0.25
    elif demand_factor == "MEDIUM":
        demand_adjustment = base_fare * 0.10
    else:
        demand_adjustment = 0

    # -------------------------
    # Final dynamic price
    # -------------------------
    final_price = base_fare + seat_factor + time_factor + demand_adjustment

    return round(final_price, 2)
