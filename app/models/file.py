from pydantic import BaseModel
from datetime import datetime

class File(BaseModel):
    name: str
    size_in_bytes: int
    created_at: datetime
    updated_at: datetime
