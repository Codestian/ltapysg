from .api import call

# Retrieve arrival timings for all buses operating for specified bus stop. Each bus has 3 recurring timings.
async def get_bus_arrival(api_key, bus_stop_code):
    data = await call(api_key, "BusArrivalv2?BusStopCode=" + bus_stop_code)
    return data["Services"]


# Retrieve data of all operating bus services.
async def get_bus_services(api_key):
    data = await call(api_key, "BusServices")
    return data["value"]


# Retrieve data of all operating bus routes.
async def get_bus_routes(api_key):
    data = await call(api_key, "BusRoutes")
    return data["value"]


# Retrieve data of bus stops.
async def get_bus_stops(api_key):
    data = await call(api_key, "BusStops")
    return data["value"]
