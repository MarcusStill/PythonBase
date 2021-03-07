from api import *
import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy.orm import session
# from sqlalchemy import MetaData
#Win10 Traceback (most recent call last)
from functools import wraps
from asyncio.proactor_events import _ProactorBasePipeTransport


engine = create_engine("sqlite:///quote_3.db", echo=False)
Base = declarative_base(bind=engine)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String, nullable=True, unique=True)


class Tags(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    description = Column(String, nullable=True, unique=True)


class Quote(Base):
    __tablename__ = 'quote'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    text = Column(String, nullable=True, unique=True)
    author_id = Column(Integer, ForeignKey('author.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    author = relationship("Author", backref="quotes")
    tags = relationship("Tags", backref="quotes")


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

def create_tag(description: str) -> Tags:
    add_tag = Tags(description=description)
    session.add(add_tag)
    session.commit()
    return add_tag


def create_author(name: str) -> Author:
    add_author = Author(name=name)
    session.add(add_author)
    session.commit()
    return add_author

def create_quote(text: str, author_id: int, tag_id: int) -> Quote:
    add_quote = Quote(text=text, author_id=author_id, tag_id=tag_id)
    session.add(add_quote)
    session.commit()
    return add_quote

if __name__ == "__main__":
    try:
        print(
        "Запрашиваем случайные цитаты с сайта favqs.com. Поиск останавливается когда номер цитаты без остатка делится на число 'n'.")
        n = int(input('Введите число n: '))
        k = 0
        while k != 1:
            quote = asyncio.run(get_quote())
            id = int(quote['id'])
            if id % n == 0:
                k = 1
                logger.info("Result. Id qoute: {}. Author: {}. Tags: {}. Quote: {}.", quote['id'], quote['author'], quote['tags'], quote['body'])
                search_id = quote['id']
                search_author = quote['author']
                search_tag = quote['tags']
                search_quote = quote['body']
    except:
        print("Ошибка при обращении к api. Сервис недоступен.")

    else:
        Base.metadata.create_all(engine)
        session = Session()

        # Win10 Traceback (most recent call last)
        _ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)

        # search_id = "1"
        # search_author = "Bob Marley"
        # search_tag = "music"
        # search_quote = "No woman, no cry"

        # search_id = "2"
        # search_author = "Queen"
        # search_tag = "music"
        # search_quote = "We are the champion"

        print("Ищем в БД цитату с id", search_id)
        s_id = session.query(Quote).filter_by(id=search_id).first()
        if not s_id:
            print("Цитата не найдена.")
            print("Ищем автора")
            s_author = session.query(Author).filter_by(name=search_author).first()
            if not s_author:
                print("Автор не найден")
                print("Ищем tag")
                s_tag = session.query(Tags).filter_by(description=search_tag).first()
                if not s_tag:
                    print("Tag не найден")
                    print("Записываем tag")
                    create_tag(search_tag)
                    # add_tag = Tags(description=search_tag)
                    # session.add(add_tag)
                    # session.commit()
                else:
                    print("Tag найден")
                print("Записываем автора ---> и записываем цитату ---> и записываем tag")
                # add_author = Author(name=search_author)
                # session.add(add_author)
                # session.commit()
                create_author(search_author)
                print("Получаем id автора, tag и записываем цитату")
                s_author = session.query(Author).filter_by(name=search_author).first()
                s_tag = session.query(Tags).filter_by(description=search_tag).first()
                # add_quote = Quote(author_id=s_author.id, tag_id=s_tag.id, text=search_quote)
                # session.add(add_quote)
                # session.commit()
                create_quote(search_quote, s_author.id, s_tag.id)
            else:
                print("Автор найден")
                print("Получаем id автора, tag и записываем цитату")
                s_author = session.query(Author).filter_by(name=search_author).first()
                s_tag = session.query(Tags).filter_by(description=search_tag).first()
                # add_quote = Quote(author_id=s_author.id, tag_id=s_tag.id, text=search_quote)
                # session.add(add_quote)
                # session.commit()
                create_quote(search_quote, s_author.id, s_tag.id)
        else:
            print("Цитата найдена. Ничего не делаем")

        session.close()
    finally:
        print("Программа завершила свою работу.")
