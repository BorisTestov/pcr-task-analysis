from datetime import date

from pydantic import BaseModel, Field

from core.constants import MAX_SPRINT_NUMBER, MIN_SPRINT_NUMBER


class SprintStatistics(BaseModel):
    total_students: int = Field(ge=0)
    sprint: int = Field(ge=MIN_SPRINT_NUMBER, le=MAX_SPRINT_NUMBER)


class Statistics(BaseModel):
    total_students: int = Field(ge=0)
    total_tasks: int = Field(ge=0)
    sprints_statistics: list[SprintStatistics] = Field(default_factory=list)
    first_task_date: date
    last_task_date: date
