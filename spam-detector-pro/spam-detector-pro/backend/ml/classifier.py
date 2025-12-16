import pickle
import os
from .preprocess import clean_text

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")


def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)

    return model, vectorizer


def predict_spam(model, vectorizer, text: str):
    text = clean_text(text)
    X = vectorizer.transform([text])
    prob = model.predict_proba(X)[0][1]
    label = "spam" if prob > 0.5 else "ham"
    return label, float(prob)
