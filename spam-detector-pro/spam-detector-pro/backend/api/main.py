from fastapi import FastAPI
from pydantic import BaseModel
from backend.ml.classifier import load_model, predict_spam
from backend.ml.utils import clean_text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS so the frontend can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load ML model
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
