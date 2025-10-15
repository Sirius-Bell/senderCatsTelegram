"""Get cat url"""
import aiohttp

async def get_cat_url():
    """Get url cat"""
    async with aiohttp.ClientSession() as session:
        async with session.get('https://cataas.com/cat?json=true') as response:
            data = await response.json()
    return data['url']
