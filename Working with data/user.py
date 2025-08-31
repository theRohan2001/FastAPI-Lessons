from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from database import Base

class UserDb(Base):
    __tablename__ = "users"

    id : Mapped[str] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)

