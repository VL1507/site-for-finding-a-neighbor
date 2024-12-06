# from fastapi import FastAPI
# from fastapi.testclient import TestClient
# from sqlalchemy.ext.asyncio import (
#     AsyncAttrs,
#     async_sessionmaker,
#     create_async_engine,
#     AsyncSession,
# )
# from main import app
# from utils.access_token import create_access_token
# from database.models import get_session

# client = TestClient(app)

# test_DB_URL = "sqlite+aiosqlite:///db.sqlite3"

# engin = create_async_engine(test_DB_URL, echo=True)

# test_async_session = async_sessionmaker(engin, expire_on_commit=False)


# async def overrides_get_session():
#     async with test_async_session() as session:
#         yield session


# app.dependency_overrides[get_session] = overrides_get_session
