from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    team_number: int = -1
    division: str = "None"

class Attendance(BaseModel):
    id: int
    date: datetime
    mode: Literal["in", "out"]
    user: User
