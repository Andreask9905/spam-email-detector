from fastapi import FastAPI
from pydantic import BaseModel
from classifier import load_model, predict_spam
from utils import clean_text

app = FastAPI()

model, vectorizer = load_model()

class EmailRequest(BaseModel):
    text: str

@app.post("/predict")
def predict_email(req: EmailRequest):
    cleaned = clean_text(req.text)
    label, prob = predict_spam(model, vectorizer, cleaned)

    return {
        "label": label,
        "probability": prob
    }

@app.get("/")
def root():
    return {"message": "Spam Detector API is running!"}
