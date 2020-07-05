from aiohttp import ClientSession, ClientConnectorError

BASE_URL = "http://datamall2.mytransport.sg/ltaodataservice/"

# Base async function to call api, receive response and handle errors.
async def call(api_key, url):
    async with ClientSession() as session:
        try:
            async with session.get(
                BASE_URL + url,
                headers={"Accept": "application/json", "AccountKey": api_key},
            ) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return "Error", "Unable to complete request"
        except ClientConnectorError as err:
            return "Error", str(err)