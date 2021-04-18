import aiohttp
import json


async def fetch_json():
    async with aiohttp.ClientSession() as session:
        params = {'limit': '1'}
        async with session.get('https://breakingbadapi.com/api/character/random', params=params) as response:
            data = json.loads(await response.text())
            fields = (data[0]['name'], data[0]['nickname'])
        await session.close()
        return fields
