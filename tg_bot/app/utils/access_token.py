from typing import Any
from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


def create_access_token(data: dict, minutes: float) -> str:
    to_encode = data.copy()
    expire = datetime.now(tz=timezone.utc) + timedelta(minutes=minutes)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encode_jwt


def decode_access_token(token: str) -> dict[str, Any]:
    decode_data = jwt.decode(token, SECRET_KEY, ALGORITHM)
    return decode_data
