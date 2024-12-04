from sqlalchemy import Sequence, select
from database.models import Profile
from database.repository import Repository


class ProfileRepository(Repository[Profile]):
    table = Profile
