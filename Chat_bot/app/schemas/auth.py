from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    username: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime
