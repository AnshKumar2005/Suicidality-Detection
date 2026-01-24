import pandas as pd
import re
import nltk
import emoji
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# -----------------------------
# NLTK downloads (run once)
# -----------------------------
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

# -----------------------------
# Stopwords (keep negations)
# -----------------------------
stop_words = set(stopwords.words("english"))
negations = {"no", "not", "never", "nothing", "none", "alone"}
stop_words = stop_words - negations

lemmatizer = WordNetLemmatizer()

# -----------------------------
# Preprocessing function
# RETURNS TOKENS (LIST)
# -----------------------------
def preprocess_text(text):
    if not text:
        return []

    text = text.lower()
    text = emoji.demojize(text, delimiters=(" ", " "))
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^a-z_: ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    tokens = text.split()
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]

    return tokens

# -----------------------------
# Function to process ONE txt file
# -----------------------------
def process_txt_file(input_path, output_path):
    original_texts = []
    tokenized_texts = []
    labels = []

    with open(input_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            # Split text and label (label is last element)
            parts = line.rsplit(maxsplit=1)

            if len(parts) != 2:
                continue  # skip malformed lines

            text, label = parts
            label = int(label)

            original_texts.append(text)
            tokenized_texts.append(preprocess_text(text))
            labels.append(label)

    df = pd.DataFrame({
        "original_text": original_texts,
        "text_tokens": tokenized_texts,
        "suicidal_label": labels
    })

    df.to_excel(output_path, index=False)
    print(f"Saved: {output_path}")

# -----------------------------
# PROCESS ALL THREE FILES
# -----------------------------
process_txt_file(
    "C:/Users/User/Downloads/SuicidEmoji/train.txt",
    "C:/Users/User/Downloads/train_preprocessed.xlsx"
)

process_txt_file(
    "C:/Users/User/Downloads/SuicidEmoji/val.txt",
    "C:/Users/User/Downloads/val_preprocessed.xlsx"
)

process_txt_file(
    "C:/Users/User/Downloads/SuicidEmoji/test.txt",
    "C:/Users/User/Downloads/test_preprocessed.xlsx"
)
