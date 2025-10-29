import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
import joblib
import os

DATA_PATH = "data/sample.csv"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "spam_model.joblib")

def load_data(path):
    df = pd.read_csv(path)
    df["label"] = df["label"].map({"ham": 0, "spam": 1})
    return df

def build_model():
    return Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english")),
        ("clf", LogisticRegression(max_iter=200))
    ])

def main():
    os.makedirs(MODEL_DIR, exist_ok=True)
    data = load_data(DATA_PATH)
    X_train, X_test, y_train, y_test = train_test_split(
        data["text"], data["label"], test_size=0.2, random_state=42
    )

    model = build_model()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))
    print("\nClassification Report:\n", classification_report(y_test, predictions))

    joblib.dump(model, MODEL_PATH)
    print(f"✅ Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()
