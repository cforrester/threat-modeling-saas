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
    components: List[Any]

@router.post("/threat-models")
def create_threat_model(threat_model: ThreatModelCreate, db: Session = Depends(get_db)):
    threats = analyze_threats(threat_model.components, db)
    
    new_model = ThreatModel(
        name=threat_model.name,
        components=threat_model.components,
        threats=threats,
        created_by=1  # Replace with authenticated user ID
    )
    
    db.add(new_model)
    db.commit()
    db.refresh(new_model)
    
    return new_model

@router.get("/threat-models")
def get_threat_models():
    # Return a list of threat models from the DB
    # This could be an ORM query, for example:
    # models = db.query(ThreatModel).all()
    # return models
    return [
        {
            "id": 1,
            "name": "Example Model",
            "created_by": 1,
            "created_at": "2025-02-17T20:00:00",
            "components": [
                {"name": "Database", "type": "database"},
                {"name": "API", "type": "api"}
            ],
            "threats": [
                {"name": "SQL Injection", "risk_level": "High"}
            ]
        }
    ]