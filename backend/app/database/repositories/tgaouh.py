from sqlalchemy import Sequence, select
from database.models import TgAouh
from database.repository import Repository


class TgAouhRepository(Repository[TgAouh]):
    table = TgAouh
