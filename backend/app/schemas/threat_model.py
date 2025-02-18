from pydantic import BaseModel
from typing import List
from app.schemas.component import Component

class ThreatModelCreate(BaseModel):
    name: str
    components: List[Component]
