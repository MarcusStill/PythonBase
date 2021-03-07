from api import *
import datetime
import asyncio
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///quote3.db", echo=True)
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
    try:
        print("Запрашиваем случайные цитаты с сайта favqs.com. Поиск останавливается когда номер цитаты без остатка делится на число 'n'.")
        n = int(input('Введите число n: '))
        k = 0
        while k != 1:
            quote = asyncio.run(get_quote())
            id = int(quote['id'])
            if id % n == 0:
                k = 1
                print("Результат. Id цитаты:", quote['id'], "Автор:", quote['author'], "Теги:", quote['tags'], "Текст:", quote['body'])
                search_id = quote['id']
                search_author = quote['author']
                tag_list = quote['tags']
                if not tag_list:
                    tag_list = '-'
                else:
                    search_tag = (', '.join(tag_list))
                search_quote = quote['body']
    except:
        print("Ошибка при обращении к api. Сервис недоступен.")
    else:
        Base.metadata.create_all(engine)
        session = Session()
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
                else:
                    print("Tag найден")
                print("Записываем автора")
                create_author(search_author)
                print("Получаем id автора, tag и записываем цитату")
                s_author = session.query(Author).filter_by(name=search_author).first()
                s_tag = session.query(Tags).filter_by(description=search_tag).first()
                create_quote(search_quote, s_author.id, s_tag.id)
            else:
                print("Автор найден")
                print("Получаем id автора, tag и записываем цитату")
                s_author = session.query(Author).filter_by(name=search_author).first()
                s_tag = session.query(Tags).filter_by(description=search_tag).first()
                create_quote(search_quote, s_author.id, s_tag.id)
        else:
            print("Цитата найдена. Ничего не делаем")
        session.close()
    finally:
        print("Программа завершила свою работу.")
