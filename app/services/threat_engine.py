# app/services/threat_engine.py
def analyze_threats(components: list) -> list:
    detected_threats = []
    # For each component, check for a missing authentication flag as a sample rule.
    for component in components:
        if not component.get("authentication", False):
            detected_threats.append({
                "category": "Spoofing",
                "riskLevel": "High",
                "recommendation": "Implement authentication for this component."
            })
    return detected_threats
