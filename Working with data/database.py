from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine


DATABASE_URL = "sqlite:///./users.db"

class Base(DeclarativeBase):
    pass

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)