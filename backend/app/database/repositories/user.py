from database.models import User
from database.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User
