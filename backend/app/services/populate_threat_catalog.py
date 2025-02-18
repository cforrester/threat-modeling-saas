from sqlalchemy.orm import Session
from app.models.threat_catalog import ThreatCatalog

THREAT_DATA = [
    # OWASP Top 10
    {
        "name": "SQL Injection",
        "owasp_category": "Injection",
        "stride_category": "Tampering",
        "risk_level": "Critical",
        "description": "Allows attackers to execute arbitrary SQL queries.",
        "mitigation": "Use prepared statements and parameterized queries.",
        "reference": "https://owasp.org/www-project-top-ten/2017/A1_2017-Injection"
    },
    {
        "name": "Broken Authentication",
        "owasp_category": "Broken Authentication",
        "stride_category": "Spoofing",
        "risk_level": "Critical",
        "description": "Weak authentication mechanisms allow attackers to impersonate users.",
        "mitigation": "Implement multi-factor authentication and strong password policies.",
        "reference": "https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication"
    },
    {
        "name": "Sensitive Data Exposure",
        "owasp_category": "Sensitive Data Exposure",
        "stride_category": "Information Disclosure",
        "risk_level": "High",
        "description": "Sensitive data can be exposed due to inadequate protection.",
        "mitigation": "Encrypt data at rest and in transit, and use proper key management.",
        "reference": "https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure"
    },
    {
        "name": "Cross-Site Scripting (XSS)",
        "owasp_category": "Cross-Site Scripting (XSS)",
        "stride_category": "Information Disclosure",
        "risk_level": "High",
        "description": "Allows attackers to inject malicious scripts into webpages.",
        "mitigation": "Sanitize and encode user inputs.",
        "reference": "https://owasp.org/www-project-top-ten/2017/A7_2017-Cross-Site_Scripting_(XSS)"
    },
    # STRIDE-specific threats or those not directly in OWASP Top 10
    {
        "name": "Repudiation",
        "owasp_category": None,
        "stride_category": "Repudiation",
        "risk_level": "Medium",
        "description": "Users or attackers may deny performing actions without proper audit logs.",
        "mitigation": "Implement comprehensive logging and non-repudiation controls.",
        "reference": "https://docs.microsoft.com/en-us/security/compass/stride"
    },
    {
        "name": "Denial of Service",
        "owasp_category": None,
        "stride_category": "Denial of Service",
        "risk_level": "High",
        "description": "Attackers can disrupt service availability by overwhelming resources.",
        "mitigation": "Implement rate limiting, load balancing, and resource management.",
        "reference": "https://owasp.org/www-project-top-ten/2017/A9_2017-Using_Components_with_Known_Vulnerabilities"  # or other relevant docs
    },
    {
        "name": "Elevation of Privilege",
        "owasp_category": None,
        "stride_category": "Elevation of Privilege",
        "risk_level": "Critical",
        "description": "Attackers gain unauthorized access to higher-privileged functions.",
        "mitigation": "Enforce least privilege principles and proper access controls.",
        "reference": "https://docs.microsoft.com/en-us/security/compass/stride"
    },
    # You can continue to add more threats as needed...
]

def populate_threat_catalog(db: Session):
    for threat in THREAT_DATA:
        existing = db.query(ThreatCatalog).filter_by(name=threat["name"]).first()
        if not existing:
            db.add(ThreatCatalog(**threat))
    db.commit()
