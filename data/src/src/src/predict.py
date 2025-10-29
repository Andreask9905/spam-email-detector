import joblib
import sys
import os

MODEL_PATH = "models/spam_model.joblib"

def predict_message(message):
    if not os.path.exists(MODEL_PATH):
        return "❌ Model not found. Train the model first by running train.py"
    model = joblib.load(MODEL_PATH)
    prediction = model.predict([message])[0]
    return "✅ HAM (not spam)" if prediction == 0 else "🚨 SPAM detected"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ℹ️ Usage: python src/predict.py \"your message here\"")
        sys.exit()
    message = " ".join(sys.argv[1:])
    print(predict_message(message))
