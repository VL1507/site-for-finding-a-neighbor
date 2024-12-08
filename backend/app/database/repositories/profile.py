from app.database.models import Profile
from app.database.repository import Repository


class ProfileRepository(Repository[Profile]):
    table = Profile
