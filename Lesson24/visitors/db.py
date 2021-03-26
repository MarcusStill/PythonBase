from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Visitor(Base):
    __tablename__ = 'visitor'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    gender = Column(String(3), nullable=False)


engine = create_engine('sqlite:///visitors.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


Base.metadata.create_all(engine)
