# app/services/threat_engine.py
from sqlalchemy.orm import Session
from app.models.threat_catalog import ThreatCatalog
from app.schemas.component import Component

def analyze_threats(components: list[Component], db: Session) -> list:
    detected_threats = []
    
    # Basic mapping from component type to expected threat(s)
    type_based_rules = {
        "database": "SQL Injection",
        "web_server": "Cross-Site Scripting (XSS)",
        "api": "Broken Authentication",
        "application": "Information Disclosure",
    }
    
    for comp in components:
        # Access attributes directly since comp is a Pydantic model
        comp_name = comp.name
        comp_type = comp.type.lower().strip() if comp.type else ""
        
        # Rule 1: Basic type mapping threat detection
        if comp_type in type_based_rules:
            threat_name = type_based_rules[comp_type]
            threat = db.query(ThreatCatalog).filter_by(name=threat_name).first()
            if threat:
                detected_threats.append({
                    "name": threat.name,
                    "risk_level": threat.risk_level,
                    "description": threat.description,
                    "mitigation": threat.mitigation,
                    "component": comp_name,
                    "rule": f"Component type '{comp_type}' triggers threat '{threat_name}'."
                })
        
        # Expanded Rule: Additional checks for specific types (e.g., database)
        if comp_type == "database":
            dbms = comp.dbms.lower().strip() if comp.dbms else ""
            if dbms:
                if dbms == "mysql":
                    # Check if MySQL component uses prepared statements
                    if not comp.prepared_statements:
                        threat = db.query(ThreatCatalog).filter_by(name="SQL Injection").first()
                        if threat:
                            detected_threats.append({
                                "name": threat.name,
                                "risk_level": threat.risk_level,
                                "description": threat.description,
                                "mitigation": threat.mitigation,
                                "component": comp_name,
                                "rule": "MySQL database without prepared statements detected."
                            })
                elif dbms == "postgresql":
                    # Add PostgreSQL-specific checks here if needed
                    pass
        
        # Composite Rule: Exposed components may be more vulnerable
        if comp_type in ["web_server", "api"]:
            if comp.exposed:  # Indicates external accessibility
                threat = db.query(ThreatCatalog).filter_by(name="Broken Authentication").first()
                if threat:
                    detected_threats.append({
                        "name": threat.name,
                        "risk_level": threat.risk_level,
                        "description": threat.description,
                        "mitigation": threat.mitigation,
                        "component": comp_name,
                        "rule": f"Exposed {comp_type} may be vulnerable to authentication attacks."
                    })
        
        # Rule 2: Missing authentication for components that require it
        if comp.requires_authentication and not comp.authentication:
            threat = db.query(ThreatCatalog).filter_by(name="Broken Authentication").first()
            if threat:
                detected_threats.append({
                    "name": threat.name,
                    "risk_level": threat.risk_level,
                    "description": threat.description,
                    "mitigation": threat.mitigation,
                    "component": comp_name,
                    "rule": "Missing authentication for a component that requires it."
                })
        
        # Rule 3: Sensitive data handling without encryption
        if comp.sensitive_data and not comp.encryption:
            threat = db.query(ThreatCatalog).filter_by(name="Tampering").first()
            if threat:
                detected_threats.append({
                    "name": threat.name,
                    "risk_level": threat.risk_level,
                    "description": threat.description,
                    "mitigation": threat.mitigation,
                    "component": comp_name,
                    "rule": "Component handles sensitive data but lacks proper encryption."
                })
        
        # Rule 4: Missing input validation (example for injection attacks)
        if comp.input_handling.lower() == "none":
            threat = db.query(ThreatCatalog).filter_by(name="SQL Injection").first()
            if threat:
                detected_threats.append({
                    "name": threat.name,
                    "risk_level": threat.risk_level,
                    "description": threat.description,
                    "mitigation": threat.mitigation,
                    "component": comp_name,
                    "rule": "Component lacks input validation which may lead to injection attacks."
                })
        
        # Additional rules can be added here as needed...
    
    return detected_threats
