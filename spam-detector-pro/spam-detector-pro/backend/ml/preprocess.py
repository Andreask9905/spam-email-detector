import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

def clean_email(text):
    """
    Cleans email text or HTML and prepares it for ML training.
    """

    # Remove HTML
    text = BeautifulSoup(text, "html.parser").get_text()

    # Lowercase
    text = text.lower()

    # Remove non-letters
    text = re.sub(r"[^a-z ]", " ", text)

    # Tokenize
    tokens = text.split()

    # Remove stopwords
    tokens = [t for t in tokens if t not in stop_words]

    return " ".join(tokens)
