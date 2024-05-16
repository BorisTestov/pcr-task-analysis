from datetime import date

from pydantic import BaseModel, Field

from core.constants import MAX_SPRINT_NUMBER, MIN_SPRINT_NUMBER


class Task(BaseModel):
    sprint: int = Field(ge=MIN_SPRINT_NUMBER, le=MAX_SPRINT_NUMBER)
    username: str = Field(min_length=1, max_length=100)
    date: date
