from api import *
import asyncio
from dataclasses import dataclass
from loguru import logger
import datetime
from beautifultable import BeautifulTable
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.ext.declarative import declarative_base


@dataclass
class Service:
    name: str
    url: str
    quote_field: str


engine = create_engine("sqlite:///quote3.db", echo=False)
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
    Base.metadata.create_all(engine)
    menu = int(input('Меню: 1 - работа с api, 2 - запрос информации из БД по авторам, 3 - запрос информации из БД по тегам. Ваш выбор: '))
    if (menu != 1) and (menu != 2) and (menu != 3):
        raise ValueError("Ошибка ввода! Введите 1, 2 или 3")
    else:
        if menu == 1:
            print("Запрашиваем случайные цитаты с сайта favqs.com. Поиск останавливается когда номер цитаты без остатка делится на число 'n'.")
            n = int(input('Введите число n: '))
            logger.info("Начинаем получать данные с api")
            quote = asyncio.run(get_my_quote())
            id = int(quote['id'])
            print("Результат. Id цитаты:", quote['id'], "Автор:", quote['author'], "Теги:", quote['tags'], "Текст:", quote['body'])
            search_id = quote['id']
            search_author = quote['author']
            tag_list = quote['tags']
            tag_list = quote['tags']
            if tag_list == {}:
                search_tag = '-'
            else:
                search_tag = (', '.join(tag_list))
            search_quote = quote['body']
            session = Session()
            print("Ищем в БД цитату с id", search_id)
            s_id = session.query(Quote).filter_by(id=search_id).first()
            if not s_id:
                print("Цитата не найдена. Ищем автора.")
                s_author = session.query(Author).filter_by(name=search_author).first()
                if not s_author:
                    print("Автор не найден. Ищем tag.")
                    s_tag = session.query(Tags).filter_by(description=search_tag).first()
                    if not s_tag:
                        print("Tag не найден. Записываем tag.")
                        create_tag(search_tag)
                    else:
                        print("Tag найден.")
                    print("Записываем автора.")
                    create_author(search_author)
                    print("Получаем id автора, tag и записываем цитату.")
                    s_author = session.query(Author).filter_by(name=search_author).first()
                    s_tag = session.query(Tags).filter_by(description=search_tag).first()
                    create_quote(search_quote, s_author.id, s_tag.id)
                else:
                    print("Автор найден.")
                    print("Получаем id автора, tag и записываем цитату.")
                    s_author = session.query(Author).filter_by(name=search_author).first()
                    s_tag = session.query(Tags).filter_by(description=search_tag).first()
                    create_quote(search_quote, s_author.id, s_tag.id)
            else:
                print("Цитата найдена в БД. Ничего не делаем.")
            session.close()
        elif menu == 2:
            session = Session()
            print("Список всех авторов, внесенных в БД.")
            table = BeautifulTable()
            for author in session.query(Author).order_by(Author.id):
                table.rows.append([author.id, author.name])
            table.columns.header = ["id", "Имя"]
            print(table)
            author_id = int(input('Для показа всех цитат одного автора введите его id: '))
            table = BeautifulTable()
            query = session.query(Author, Quote)
            query = query.join(Quote, Quote.author_id == Author.id)
            records = query.filter_by(author_id=author_id)
            for author, quote in records:
                table.rows.append([quote.text])
            table.columns.header = ["Все записи этого автора"]
            print(table)
            session.close()
        elif menu == 3:
            session = Session()
            print("Список всех тегов, внесенных в БД.")
            table = BeautifulTable()
            for tags in session.query(Tags).order_by(Tags.id):
                table.rows.append([tags.id, tags.description])
            table.columns.header = ["id", "Описание"]
            print(table)
            tags_id = int(input('Для показа всех цитат с одним тегом введите его id: '))
            table = BeautifulTable()
            query = session.query(Quote, Tags)
            query = query.join(Quote, Quote.tag_id == Tags.id)
            records = query.filter_by(tag_id=tags_id)
            for quote, tags in records:
                table.rows.append([quote.text])
            table.columns.header = ["Все записи c этим тегом"]
            print(table)
            session.close()
    print("Программа завершила свою работу.")
