import asyncio
from dataclasses import dataclass
from aiohttp import ClientSession
from loguru import logger


#Win10 Traceback (most recent call last)
from functools import wraps
from asyncio.proactor_events import _ProactorBasePipeTransport


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
    async with session.get(url) as response:
        return await response.json()


async def fetch_quote(service: Service) -> str:
    """
    :param service:
    :return:
    """
    async with ClientSession() as session:
        result = await fetch_json(session, service.url)

    logger.info("Fetched {}, result: {}", service.name, result)
    return result[service.quote_field]


async def get_quote():
    service = Service("favqs", "https://favqs.com/api/qotd", "quote")
    my_quote = await fetch_quote(service)
    #print(my_quote)
    #print(type(my_quote))
    logger.info("Quote: {!r}", my_quote)
    logger.info("\n id: {},\n author: {},\n qote: {}", my_quote['id'], my_quote['author'], my_quote['body'])


#Win10 Traceback (most recent call last)
def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise
    return wrapper

def run_main():
   asyncio.run(get_quote())
   _ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)

if __name__ == "__main__":
    run_main()

