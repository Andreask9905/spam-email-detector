import joblib
import numpy as np

def load_model():
    model = joblib.load("backend/ml/model.pkl")
    vectorizer = joblib.load("backend/ml/vectorizer.pkl")
    return model, vectorizer

def predict_spam(model, vectorizer, text):
    X = vectorizer.transform([text])
    prob = model.predict_proba(X)[0][1]
    pred = "spam" if prob > 0.5 else "ham"
    return pred, float(prob)
