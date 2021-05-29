import aiohttp
import asyncio
# import json


async def get_info(session, url):
    async with session.get(url) as response:
        data = await response.json()
        fields = (data[0]['name'], data[0]['nickname'])
        return fields


async def fetch_json():
    async with aiohttp.ClientSession() as session:
        # params = {'limit': '1'}
        # async with session.get('https://breakingbadapi.com/api/character/random', params=params) as response:
        #     data = json.loads(await response.text())
        #     fields = (data[0]['name'], data[0]['nickname'])
        # await session.close()
        # return fields
        tasks = []
        for number in range(1, 50):
            url = f'https://breakingbadapi.com/api/characters/{number}'
            tasks.append(asyncio.ensure_future(get_info(session, url)))

        users = await asyncio.gather(*tasks)
        data = []
        for user in users:
            data.append(user)
        return data
