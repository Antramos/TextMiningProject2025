import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK resources
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    text = text.lower()  # Lowercase
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"\$\w+", "ticker", text)  # Replace $TICKERS with 'ticker'
    text = re.sub(r"[^a-z\s]", "", text)  # Remove punctuation & numbers
    tokens = nltk.word_tokenize(text)  # Tokenization
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]  # Lemmatize & remove stopwords
    return "".join(tokens)

# Basic text cleaning for EDA

def eda_clean_text(text):
    text = re.sub(r"http\S+", "", text)        # URLs => ""
    text = re.sub(r"[$]\w+", "", text)         # $TICKERS => ""
    text = re.sub(r"[^\w\s]", "", text)        # punctuation => ""
    text = re.sub(r"\s+", " ", text)           # extra blanks => ""
    return text.strip().lower()                # text to lower

def preprocess(text):
    text = text.lower()  # Lowercase
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"\$\w+", "ticker", text)  # Replace $TICKERS with 'ticker'
    text = re.sub(r"[^a-z\s]", "", text)  # Remove punctuation & numbers
    tokens = nltk.word_tokenize(text)  # Tokenization
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]  # Lemmatize & remove stopwords
    return " ".join(tokens)
