from numpy._core.fromnumeric import transpose
import pandas as pd
import time
import regex as re
from googletrans import Translator
from tqdm import tqdm

def trans(INPUT_FILE, OUTPUT_FILE):
  TOKEN_COLUMN = "text_tokens"          # change if needed
  TRANSLATED_COLUMN = "tokens_hi"

  BATCH_SIZE = 100
  SRC_LANG = "en"
  DEST_LANG = "hi"
  # ==========================================


  # ================= LOAD DATA =================
  df = pd.read_excel(INPUT_FILE, engine="openpyxl")

  if TOKEN_COLUMN not in df.columns:
      raise ValueError(f"Column '{TOKEN_COLUMN}' not found")

  translator = Translator()


  # ================= EMOJI-TEXT DETECTOR =================
  def is_emoji_text(token):
      if pd.isna(token):
          return True

      token = str(token).strip()

      # Real emoji (unicode)
      if any(ord(ch) > 10000 for ch in token):
          return True

      # Emoji-text patterns: smiling_face, face_with_tears_of_joy
      if (
          "_" in token and
          token.islower() and
          " " not in token and
          len(token) <= 40
      ):
          return True

      return False


  # ================= TRANSLATION =================
  unique_tokens = df[TOKEN_COLUMN].dropna().unique()

  token_map = {}

  # Translate only NON emoji-text tokens
  translatable_tokens = [t for t in unique_tokens if not is_emoji_text(t)]

  print(f"Total tokens        : {len(unique_tokens)}")
  print(f"Translated tokens   : {len(translatable_tokens)}")
  print(f"Preserved emojis    : {len(unique_tokens) - len(translatable_tokens)}")

  for start in tqdm(range(0, len(translatable_tokens), BATCH_SIZE)):
      batch = translatable_tokens[start:start + BATCH_SIZE]

      for token in batch:
          try:
              token_map[token] = translator.translate(
                  token[:200], src=SRC_LANG, dest=DEST_LANG
              ).text
          except:
              token_map[token] = token  # fail-safe

      time.sleep(1)  # prevent rate limiting

  # Preserve emoji-text tokens as-is
  for token in unique_tokens:
      if token not in token_map:
          token_map[token] = token

  # Map back to dataframe
  df[TRANSLATED_COLUMN] = df[TOKEN_COLUMN].map(token_map)


  # ================= SAVE (UNICODE SAFE) =================
  df.to_excel(
      OUTPUT_FILE,
      index=False,
      engine="openpyxl"
  )

  print("\n✅ Translation completed successfully!")
  print("📁 Output file:", OUTPUT_FILE)


trans(
    "C:\Users\User\Downloads\SuicidEmoji_preprocessed\train_preprocessed.xlsx",
    "translated_tokens_hindi_emoji_safe_train.xlsx"
)

trans(
    "C:\Users\User\Downloads\SuicidEmoji_preprocessed\val_preprocessed.xlsx",
    "translated_tokens_hindi_emoji_safe_val.xlsx"
)

trans(
    "C:\Users\User\Downloads\SuicidEmoji_preprocessed\test_preprocessed.xlsx",
    "translated_tokens_hindi_emoji_safe_test.xlsx"
)
