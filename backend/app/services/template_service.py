import random
from app.utils.file_loader import load_json

def load_template(industry: str, experience: str):
    path = f"app/data/templates/{industry.lower()}/{experience.lower()}.json"
    template = load_json(path)
    return template