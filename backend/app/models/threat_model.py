from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from app.config.database import Base  # ✅ Use the shared Base

class ThreatModel(Base):
    __tablename__ = "threat_models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    components = Column(JSON)  # Stores system components
    created_by = Column(Integer, ForeignKey("users.id"))
