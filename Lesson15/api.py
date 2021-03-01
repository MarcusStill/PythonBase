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
    logger.info("Received quote: {}", result)
    return result[service.quote_field]


async def get_quote():
    service = Service("favqs.com", "https://favqs.com/api/qotd", "quote")
    my_quote = await fetch_quote(service)
    return my_quote


# def run_main_async():
#     logger.info("Start async main")
#     coros = [
#         get_quote(),
#         get_quote(),
#     ]
#     task = asyncio.wait(coros)
#     asyncio.run(task)
#     logger.info("Finish async main")


def run_main():
    print("Программа запрашивает случайные цитаты с сайта favqs.com. Поиск останавливается когда номер цитаты без остатка делится на число 'n'.")
    n = int(input('Введите число n: '))
    k = 0
    while k != 1:
        quote = asyncio.run(get_quote())
        id = int(quote['id'])
        if id % n == 0:
            k = 1
            logger.info("Result. Id qoute: {}. Author: {}. Quote: {}", quote['id'], quote['author'], quote['body'])
    #Win10 Traceback (most recent call last)
    _ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)

if __name__ == "__main__":
    run_main()

