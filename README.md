# ✉️ Spam Email Detector (Machine Learning Project)

Ένα απλό αλλά λειτουργικό μοντέλο ταξινόμησης spam/ham emails με Python και Scikit-learn.

---

## 📘 Περιγραφή
Το project περιλαμβάνει κώδικα για:
- Εκπαίδευση μοντέλου (`src/train.py`)
- Πρόβλεψη νέων μηνυμάτων (`src/predict.py`)
- Γρήγορη εκτέλεση μέσω μενού (`main.py`)

---

## 📂 Δομή φακέλων
spam-email-detector/
├─ data/
│  ├─ sample.csv
├─ src/
│  ├─ train.py
│  ├─ predict.py
├─ main.py
├─ requirements.txt
└─ .gitignore
---

## ⚙️ Εγκατάσταση
```bash
pip install -r requirements.txt
---
---

## 🧠 Εκπαίδευση Μοντέλου
```bash
python src/train.py
- Εκπαιδεύει Logistic Regression με TF-IDF vectorizer  
- Αποθηκεύει το μοντέλο στο `models/spam_model.joblib`

---

## 🔍 Πρόβλεψη
```bash
python src/predict.py "Your message here"
ή τρέξε το κύριο αρχείο:
```bash
python main.py
---

## 🛠️ Τεχνολογίες
- Python  
- Pandas  
- Scikit-learn  
- Joblib  

---

## 🚀 Μελλοντικές ιδέες
- Streamlit web UI  
- Εναλλακτικά μοντέλα (Naive Bayes, SVM)  
- Εμπλουτισμένο preprocessing  

---

## 👤 Δημιουργός
**Andreas Koutsoventis**  
[LinkedIn](https://www.linkedin.com/in/andreas-koutsoventis-2b884733a)  
*Junior Python Developer | AI & Machine Learning Enthusiast*




