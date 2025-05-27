import re ## regular expressions

# Basic text cleaning for EDA

def eda_clean_text(text):
    text = re.sub(r"http\S+", "", text)        # URLs => ""
    text = re.sub(r"[$]\w+", "", text)         # $TICKERS => ""
    text = re.sub(r"[^\w\s]", "", text)        # punctuation => ""
    text = re.sub(r"\s+", " ", text)           # extra blanks => ""
    return text.strip().lower()                # text to lower