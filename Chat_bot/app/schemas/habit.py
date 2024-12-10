from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class HabitSchema(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: datetime
    frequency: str
