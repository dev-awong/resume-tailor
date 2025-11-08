import re

def extract_keywords(text: str):
    # Very primitive keyword extraction, first version
    keywords = set(re.findall(r"\b[A-Za-z]+\b", text))
    return list(keywords)

