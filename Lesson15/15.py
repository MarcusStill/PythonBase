# from db import *
from api import *
#Win10 Traceback (most recent call last)
from functools import wraps
from asyncio.proactor_events import _ProactorBasePipeTransport

from sqlalchemy import create_engine, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///quote.db", echo=True)
Base = declarative_base(bind=engine)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(100), unique=True)


class Quote(Base):
    __tablename__ = 'quote'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    text = Column(String, nullable=True, unique=True)
    author_id = Column(Integer, ForeignKey('author.id'))
    created_at = Column(String)

    author = relationship("Author", backref="quotes")


def create_author(name: str) -> Author:
    new_author = Author(name=name)
    print("Id before", new_author.id)
    session.add(new_author)
    session.commit()
    print("Id after", new_author.id)
    return new_author


def create_quote(text: str, author_id: int, created_at: str) -> Quote:
    new_quote = Quote(text=text, author_id=author_id, created_at=created_at)
    print("id before", new_quote.id)
    session.add(new_quote)
    session.commit()
    print("id after", new_quote.id)
    return new_quote



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


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Запрашиваем случайные цитаты с сайта favqs.com. Поиск останавливается когда номер цитаты без остатка делится на число 'n'.")
    n = int(input('Введите число n: '))
    k = 0
    while k != 1:
        quote = asyncio.run(get_quote())
        id = int(quote['id'])
        if id % n == 0:
            k = 1
            logger.info("Result. Id qoute: {}. Author: {}. Quote: {}", quote['id'], quote['author'], quote['body'])
            #print(quote['id'])
            search_quote = quote['id']
            search_author = quote['author']
            insert_quote = quote['body']


    # Win10 Traceback (most recent call last)
    _ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)


    session = Session()
    # # new_author = create_author("Bob Marley")
    # print("Print all Author")
    # for instance in session.query(Author).order_by(Author.id):
    #     print("id", instance.id, instance.name)
    # # new_quote = create_quote("Life is good", "1", "2021-03-02")
    # # new_quote = create_quote("No Woman, no cry", "1", "2021-03-03")
    #
    # print("Print all quote one author")
    # for instance in session.query(Quote).order_by(Quote.id):
    #     print("id", instance.id, instance.text, "author_id", instance.author_id, instance.created_at)
    #
    # print("Print all quotes one Author")
    # query = session.query(Author, Quote)
    # query = query.join(Quote, Quote.author_id == Author.id)
    # records = query.all()
    # print(records)
    # for author, quote in records:
    #     print(author.name, "-", quote.text)
    #
    # """
    # Логика
    # """
    result = 0
    print("Ищем в БД цитату с id", search_quote)
    for Quote in session.query(Quote.id).filter_by(id=search_quote):
        result = 1
    if not result:
        print('Цитата с таким id в БД не найдена')
        print("Ищем автора в БД", search_author)
        for Quote in session.query(Author).filter_by(name=search_author):
            result = 2
        if result == 2:
            print('Запрашиваемый автор в БД не найден')
            #new_author = create_author(search_author)
            new_author = create_author("12345")
            #new_author = create_author(search_author)
            #new_quote = create_quote(insert_quote, new_author.id, "2021-03-05")
            #new_author.id
        else:
            print('Запрашиваемый автор в БД найден')
    else:
        print("Цитата с таким id найдена в БД")

    session.close()

    """
    Добавление цитаты.
        - поиск в БД по номеру. Если цитата с таким номером есть  -->  не вносим.
        - если номера в БД нет --> Ищем автора. Если такой автор есть, то берем его номер и записываем цитату.
        - если автора нет  --> вносим автора, берем его номер и записываем цитату.

    """

