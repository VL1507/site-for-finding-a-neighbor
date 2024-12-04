from pydantic import BaseModel


class SProfile(BaseModel):
    name: str
    gender: str
    status: str
    smoking: str
    go_to_bed_at: str
    get_up_in: str