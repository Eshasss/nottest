from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    password: Mapped[str] = mapped_column(String(20))
    tokens: Mapped[List["Token"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class Token(Base):
    __tablename__ = "tokens_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    token: Mapped[str]
    user: Mapped["User"] = relationship(back_populates="tokens")
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))

engine = create_engine("sqlite:///test.db", echo = True)

Base.metadata.create_all(bind = engine)


