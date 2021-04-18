from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import rapi


engine = create_engine("postgresql://user:qweasds121@localhost:5432/postgres", echo=True)
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    nickname = Column(String)


async def create_user():
    session = Session()

    fields = await rapi.fetch_json()
    name, nickname = fields

    ed_user = User(name=name, nickname=nickname)
    session.add(ed_user)
    session.commit()

    session.close()
