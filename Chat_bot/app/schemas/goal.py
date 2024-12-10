from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class GoalSchema(BaseModel):
    name: str
    target_date: datetime
    description: Optional[str] = None
    progress: Optional[int] = 0
