import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
from preprocess import clean_email

# Load dataset (change this path if needed)
df = pd.read_csv("datasets/enron.csv")  # Ensure this dataset exists
df["clean"] = df["text"].apply(clean_email)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    df["clean"], df["label"], test_size=0.2, random_state=42
)

# Vectorizer
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = LogisticRegression(max_iter=2000)
model.fit(X_train_vec, y_train)

# Evaluation
print(classification_report(y_test, model.predict(X_test_vec)))

# Save model files
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
