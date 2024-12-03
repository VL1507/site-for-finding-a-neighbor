from database.models import Profile
from database.repository import SQLAlchemyRepository


class ProfileRepository(SQLAlchemyRepository):
    model = Profile
