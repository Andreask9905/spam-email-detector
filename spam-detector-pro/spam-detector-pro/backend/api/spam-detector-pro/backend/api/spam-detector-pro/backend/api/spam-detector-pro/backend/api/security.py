import re

def analyze_urls(urls):
    """
    Analyzes a list of URLs and identifies possible phishing indicators.
    Returns a report with warnings for each URL.
    """

    report = []

    suspicious_keywords = [
        "login", "verify", "update", "bank", "secure", "password",
        "account", "confirm", "unlock", "reset"
    ]

    for url in urls:
        entry = {"url": url, "warnings": []}

        # 1. Non-secure URL
        if url.startswith("http://"):
            entry["warnings"].append("⚠️ Non-secure URL (HTTP instead of HTTPS)")

        # 2. Suspicious keywords
        if any(word in url.lower() for word in suspicious_keywords):
            entry["warnings"].append("⚠️ URL contains suspicious phishing keywords")

        # 3. Unicode letters (homograph attack)
        if re.search(r"[^\x00-\x7F]", url):
            entry["warnings"].append("⚠️ Unicode characters detected (possible homograph attack)")

        report.append(entry)

    return report
