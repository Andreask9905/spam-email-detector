from fastapi import FastAPI
from pydantic import BaseModel
from .classifier import load_model, predict_spam
from .utils import extract_text_from_html, extract_urls
from .security import analyze_urls

app = FastAPI(
    title="Spam Detector PRO",
    description="Advanced spam & phishing detection API",
    version="1.0"
)

class EmailInput(BaseModel):
    email_content: str

model, vectorizer = load_model()

@app.post("/predict")
def predict(email: EmailInput):
    html_text = extract_text_from_html(email.email_content)
    urls = extract_urls(email.email_content)
    phishing_report = analyze_urls(urls)

    prediction, prob = predict_spam(model, vectorizer, html_text)
    return {
        "prediction": prediction,
        "probability": prob,
        "urls_found": urls,
        "phishing_report": phishing_report
    }

@app.get("/health")
def health():
    return {"status": "ok"}
