import os
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine(os.environ['SQL_URL'])
session_maker = sessionmaker(bind=engine)

