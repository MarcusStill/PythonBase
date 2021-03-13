import asyncio
from aiohttp import ClientSession
from dataclasses import dataclass
from loguru import logger

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
    logger.info("Fetching {}", service.name)
    async with ClientSession() as session:
        result = await fetch_json(session, service.url)
    return result[service.quote_field]


async def get_my_quote():
    coro = asyncio.wait(
        {
            asyncio.create_task(fetch_quote(Service("favqs.com", "https://favqs.com/api/qotd", "quote")))
            for i in range(29)
        },
        timeout=10,
        return_when=asyncio.FIRST_COMPLETED,
    )

    done, pending = await coro

    for task in pending:
        logger.debug("Cancelling task {}", task)
        task.cancel()

    my_quote = None
    for task in done:
        my_quote = task.result()
        break
    else:
        logger.warning("No results found!")

    return my_quote
