from bs4 import BeautifulSoup
import re

def extract_text_from_html(html):
    """
    Converts HTML email content to plain readable text.
    """
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    return text

def extract_urls(text):
    """
    Extracts all URLs from an input email (HTML or plain text).
    """
    url_regex = r"https?://[^\s]+"
    return re.findall(url_regex, text)
