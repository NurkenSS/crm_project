from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ReminderSchema(BaseModel):
    message: str
    remind_at: datetime
    habit_id: Optional[int] = None
    goal_id: Optional[int] = None
