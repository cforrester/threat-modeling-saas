from sqlalchemy import Column, Integer, String, Text
from app.config.database import Base

class ThreatCatalog(Base):
    __tablename__ = "threat_catalog"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)  # Threat name
    category = Column(String, index=True)  # STRIDE category, OWASP classification
    risk_level = Column(String)  # Low, Medium, High, Critical
    description = Column(Text)  # Details about the threat
    mitigation = Column(Text)  # Suggested security fix
