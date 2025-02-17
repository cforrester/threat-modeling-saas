# app/services/report_service.py
import pdfkit
from jinja2 import Environment, FileSystemLoader
import os

def generate_pdf_report(threat_model: dict) -> bytes:
    # Set up Jinja2 environment to load HTML templates
    env = Environment(loader=FileSystemLoader(os.path.join(os.getcwd(), "app", "templates")))
    template = env.get_template("report_template.html")
    html_content = template.render(threat_model=threat_model)
    # Convert the rendered HTML to PDF
    pdf = pdfkit.from_string(html_content, False)
    return pdf
