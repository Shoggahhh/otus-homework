from sqlalchemy.util import asyncio
from models.dbm import Base, engine, create_user


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    asyncio.get_event_loop().run_until_complete(create_user())
