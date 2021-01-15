import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SERVER = os.environ['SERVER_NAME']
DATABASE = os.environ['DATABASE_TYPE']
DRIVER = os.environ['DRIVER_NAME']
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']
DATABASE_CONN = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'

engine = create_engine(DATABASE_CONN)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
