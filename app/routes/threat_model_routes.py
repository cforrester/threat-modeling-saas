# app/routes/threat_model_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Any
from app.config.database import get_db
from app.models.threat_model import ThreatModel
from app.services.threat_engine import analyze_threats

router = APIRouter()

class ThreatModelCreate(BaseModel):
    name: str
    components: List[Any]  # List of components represented as dictionaries

@router.post("/threat-models")
def create_threat_model(threat_model: ThreatModelCreate, db: Session = Depends(get_db)):
    # Analyze components for potential threats
    threats = analyze_threats(threat_model.components)
    new_model = ThreatModel(
        name=threat_model.name,
        components=threat_model.components,
        threats=threats,
        created_by=1  # Replace with dynamic user ID after adding auth dependency
    )
    db.add(new_model)
    db.commit()
    db.refresh(new_model)
    return new_model

