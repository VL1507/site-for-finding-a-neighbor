from pydantic import BaseModel


class SUser(BaseModel):
    id: int
    is_admin: bool
