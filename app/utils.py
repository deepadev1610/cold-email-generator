import re


def clean_text(text):
    """
    This utility will:
     Remove HTML tags
     Remove URLS
     Remove special characters
     Replace multiple spaces with a single space
     Trim leading/trailing whitespaces
     Remove extra whitespace

    """
    if text is None:
        return ""

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)

    # Remove special characters but keep basic punctuation and alphanumerics
    text = re.sub(r"[^\w\s\.,!?'-]", " ", text)

    # Collapse multiple whitespace characters into a single space
    text = re.sub(r"\s+", " ", text)

    # Trim leading/trailing whitespace
    text = text.strip()

    return text
