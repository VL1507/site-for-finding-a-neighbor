from typing import Any
from jose import jwt
from datetime import datetime, timedelta, timezone

from config import SECRET_KEY, ALGORITHM


def create_access_token(data: dict, minutes: float) -> str:
    to_encode = data.copy()
    expire = datetime.now(tz=timezone.utc) + timedelta(minutes=minutes)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encode_jwt


def decode_access_token(token: str) -> dict[str, Any]:
    decode_data = jwt.decode(token, SECRET_KEY, ALGORITHM)
    return decode_data
