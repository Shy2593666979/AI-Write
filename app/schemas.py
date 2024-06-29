from pydantic import BaseModel
from datetime import datetime

class modelStyle(BaseModel):
    title: str
    content: str
    creatTime: datetime

class updateStyle(BaseModel):
    title: str = None
    content: str = None
    