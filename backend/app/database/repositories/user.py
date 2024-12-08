from app.database.models import User
from app.database.repository import Repository


class UserRepository(Repository[User]):
    table = User
