from dataclasses import dataclass
from aiohttp import ClientSession


@dataclass
class Service:
    name: str
    url: str
    quote_field: str


async def fetch_json(session: ClientSession, url: str) -> dict:
    """
    :param session:
    :param url:
    :return:
    """
    async with session.get(url, ssl=False) as response:
        return await response.json()


async def fetch_quote(service: Service) -> str:
    """
    :param service:
    :return:
    """
    async with ClientSession() as session:
        result = await fetch_json(session, service.url)
    return result[service.quote_field]


async def get_quote():
    service = Service("favqs.com", "https://favqs.com/api/qotd", "quote")
    my_quote = await fetch_quote(service)
    return my_quote
