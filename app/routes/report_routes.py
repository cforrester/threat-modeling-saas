# app/routes/report_routes.py
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.threat_model import ThreatModel
from app.services.report_service import generate_pdf_report

router = APIRouter()

@router.get("/threat-models/{model_id}/report")
def get_threat_model_report(model_id: int, db: Session = Depends(get_db)):
    threat_model = db.query(ThreatModel).filter(ThreatModel.id == model_id).first()
    if not threat_model:
        raise HTTPException(status_code=404, detail="Threat model not found")
    
    # Prepare data for the report
    report_data = {
        "name": threat_model.name,
        "components": threat_model.components,
        "threats": threat_model.threats,
        "created_at": str(threat_model.created_at)
    }
    report_pdf = generate_pdf_report(report_data)
    return Response(content=report_pdf, media_type="application/pdf")


