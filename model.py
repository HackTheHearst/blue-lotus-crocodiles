from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship, backref, sessionmaker, scoped_session
from sqlalchemy.engine.url import URL
from decimal import *

engine = create_engine("postgresql+psycopg2://maggieshine@localhost/hearst", echo=True)
session = scoped_session(sessionmaker(bind=engine, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

# class declarations go here
class Matching(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True)
    url = Column(String(128))
    artist = Column(String(64))
    songname = Column(String(64))

class Gallery(Base):
    __tablename__ = "globalcounts"

    id = Column(Integer, primary_key=True)
    term = Column(String(64), unique=True)
    count = Column(Integer)

def connect():
    """
    Connects to the database and returns a session object.
    """
    global engine
    global session
    engine = create_engine("postgresql+psycopg2://maggieshine@localhost/hearst", echo=False) 
    session = scoped_session(sessionmaker(bind=engine,
                             autocommit = False,
                             autoflush = False))
    return session

def create_db():
    # connection = ENGINE.connect()
    # connection.execute("commit")
    # connection.execute("DROP DATABASE IF EXISTS golem")
    # connection.execute("commit")
    # connection.execute("CREATE DATABASE golem")
    pass

def create_tables():
    # Base.metadata.drop_all(ENGINE)
    # Base.metadata.create_all(ENGINE)
    Base.metadata.create_all(engine)