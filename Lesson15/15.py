from api import *
import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import session
#from sqlalchemy import MetaData


engine = create_engine("sqlite:///quote.db", echo=True)
Base = declarative_base(bind=engine)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String, nullable=True, unique=True)


class Quote(Base):
    __tablename__ = 'quote'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    text = Column(String, nullable=True, unique=True)
    author_id = Column(Integer, ForeignKey('author.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    author = relationship("Author", backref="quotes")


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
                logger.info("Result. Id qoute: {}. Author: {}. Quote: {}", quote['id'], quote['author'], quote['body'])
                search_id = quote['id']
                search_author = quote['author']
                search_quote = quote['body']
    except:
        print("Ошибка при обращении к api. Сервис недоступен.")

    else:
        Base.metadata.create_all(engine)
        session = Session()

        """
            Добавление цитаты.
                - поиск в БД по номеру. Если цитата с таким номером есть  -->  не вносим.
                - если номера в БД нет --> Ищем автора. Если такой автор есть, то берем его номер и записываем цитату.
                - если автора нет  --> вносим автора, берем его номер и записываем цитату.
    
        """
        print("search_author type", type(search_author))
        result = 0
        print("Ищем в БД цитату с id.", search_quote)
        for Quote in session.query(Quote).filter_by(id=search_id):
            result = 1
            logger.info(result)
        if not result:
            logger.info('Цитата с таким id в БД не найдена.')
            print('Цитата с таким id в БД не найдена.')
            logger.info("Ищем автора в БД.", search_author)
            print("Ищем автора в БД.", search_author)
            for Quote in session.query(Author).filter_by(name=search_author):
                result = 2
            if result == 2:
                logger.info('Запрашиваемый автор в БД не найден.')
                print('Запрашиваемый автор в БД не найден.')
                logger.info("Добавляем автора {}", search_author)
                print("Добавляем автора", search_author)
                add_author = Author(name=search_author)
                session.add(add_author)
                session.commit()
                logger.info("Получаем его номер и записываем цитату.")
                print("Получаем его номер и записываем цитату.")
                new_author_id = session.query(Author).filter_by(name=search_author).first()
                add_quote = Quote(text=search_quote, author_id=new_author_id)
                session.add(add_quote)
                session.commit()
            else:
                print('Запрашиваемый автор в БД найден. Получаем его номер и записываем цитату.')
                logger.info('Запрашиваемый автор в БД найден. Получаем его номер и записываем цитату.')
                new_author_id = session.query(Author).filter_by(name=search_author).first()
                add_quote = Quote(text=search_quote, author_id=new_author_id)
                session.add(add_quote)
                session.commit()
        else:
            logger.info("Цитата с таким id найдена в БД.")
            print("Цитата с таким id найдена в БД.")
        session.close()
    finally:
        print("Программа завершила свою работу.")
