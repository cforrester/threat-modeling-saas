from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.threat_catalog import ThreatCatalog
from pydantic import BaseModel
from typing import List

router = APIRouter()

class ThreatResponse(BaseModel):
    name: str
    category: str
    risk_level: str
    description: str
    mitigation: str

@router.get("/threat-catalog", response_model=List[ThreatResponse])
def get_threat_catalog(db: Session = Depends(get_db)):
    threats = db.query(ThreatCatalog).all()
    return threats
