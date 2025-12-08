import random

def get_demand_factor():
    """
    Randomly simulates demand level for each flight.
    HIGH demand → higher prices
    """
    levels = ["LOW", "MEDIUM", "HIGH"]
    weights = [0.5, 0.3, 0.2]  # LOW more likely

    return random.choices(levels, weights)[0]
