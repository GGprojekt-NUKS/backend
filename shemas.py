from typing import Optional
from pydantic import BaseModel

class Forum(BaseModel):
    text: str
    topic_id: Optional[int] = None
