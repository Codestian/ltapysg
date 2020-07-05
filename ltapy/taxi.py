from .api import call

# Retrieve data of all taxis only available for hire.
async def get_taxi_availability(api_key):
    data = await call(api_key, "Taxi-Availability")
    return data["value"]

# Retrieve data of all taxi stands.
async def get_taxi_stands(api_key):
    data = await call(api_key, "TaxiStands")
    return data["value"]
