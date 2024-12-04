from sqlalchemy import Sequence, select
from database.models import User
from database.repository import Repository


class UserRepository(Repository[User]):
    table = User
