import jwt
import copy
from typing import Any
from pathlib import Path
from datetime import datetime, timedelta, timezone

from cryptography.hazmat.primitives import serialization
from cryptography.x509 import load_pem_x509_certificate

from config import settings
from utils.custom_logger import setup_logger

logger = setup_logger(__name__)


class JWTManager:
    def __init__(self, private_key_path: Path, public_key_path: Path, minutes: float):
        self.private_key = self._get_private_key(private_key_path)
        self.x509_certificate = self._get_x509_certificate(public_key_path)
        self.algorithm = "RS256"
        self.minutes = minutes

    def _get_private_key(self, private_key_path: Path):
        private_key_text = private_key_path.read_text()
        private_key = serialization.load_pem_private_key(
            data=private_key_text.encode(), password=None
        )
        return private_key

    def _get_x509_certificate(self, public_key_path: Path):
        x509_certificate = load_pem_x509_certificate(
            public_key_path.read_text().encode()
        ).public_key()
        return x509_certificate

    def encode_jwt(self, payload: dict[str, Any]) -> str | None:
        try:
            payload_ = copy.deepcopy(payload)
            expire = datetime.now(tz=timezone.utc) + timedelta(minutes=self.minutes)
            payload_.update({"exp": expire})

            token = jwt.encode(
                payload=payload_, key=self.private_key, algorithm=self.algorithm
            )
            return token
        except Exception as e:
            logger.error("Неизвестная ошибка")
            logger.error(e)
            logger.error(type(e))

    def decode_jwt(self, token: str) -> dict[str, Any] | None:
        try:
            unverified_header = jwt.get_unverified_header(jwt=token)

            return jwt.decode(
                jwt=token,
                key=self.x509_certificate,
                algorithms=unverified_header["alg"],
            )
        except jwt.exceptions.DecodeError as e:
            logger.error(e)
            logger.error(type(e))
        except jwt.exceptions.ExpiredSignatureError as e:
            logger.error(e)
            logger.error(type(e))
        except Exception as e:
            logger.error("Неизвестная ошибка")
            logger.error(e)
            logger.error(type(e))


jwt_manager = JWTManager(
    private_key_path=settings.JWT.PRIVATE_KEY_PATH,
    public_key_path=settings.JWT.PUBLIC_KEY_PATH,
    minutes=settings.JWT.LIFE_TIME_MINUTES,
)
