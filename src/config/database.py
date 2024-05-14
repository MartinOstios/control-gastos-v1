from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from dotenv import load_dotenv

load_dotenv()
database_url = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PASS')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('DB_NAME')}"

engine = create_engine(database_url)

SessionLocal = sessionmaker(bind=engine,
    autocommit=False, autoflush=False)

Base = declarative_base()
