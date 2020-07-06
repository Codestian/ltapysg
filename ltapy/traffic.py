from .api import call

# Retrieve images of live traffic along expressways and customs checkpoints.
async def get_traffic_images(api_key):
    data = await call(api_key, "Traffic-Imagesv2")
    return data["value"]

# Returns incidents currently happening.
async def get_traffic_incidents(api_key):
    data = await call(api_key, "TrafficIncidents")
    return data["value"]