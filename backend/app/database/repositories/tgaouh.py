
from app.database.models import TgAouh
from app.database.repository import Repository


class TgAouhRepository(Repository[TgAouh]):
    table = TgAouh
