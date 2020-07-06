from .api import call

# Retrieve all bus arrival times for a bus stop. Each bus will have 3 recurring timings.
# If there are no recurring timings, NA is returned. If first timing is less than 1 minute, Arr is returned.
async def get_bus_arrival(api_key, bus_stop_code):
    data = await call(
        api_key, "BusArrivalv2?BusStopCode=" + bus_stop_code
    )
    if not data["Services"]:
        raise Exception("No bus services available")
    else:
        return data["Services"]

# Retrieve data of all operating bus services.
async def get_bus_services(api_key):
    data = await call(api_key, "BusServices")
    return data["value"]

# Retrieve data of all operating bus routes.
async def get_bus_routes(api_key):
    data = await call(api_key, "BusRoutes")
    return data["value"]

# Retrieve data of bus stops 
async def get_bus_stops(api_key):
    data = await call(api_key, "BusStops")
    return data["value"]    