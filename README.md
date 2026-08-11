# **Suicidality-Detection**
**Emoji-Aware Multilingual Suicidality Detection Using Hybrid Gated Transformer Architecture**

---

## **Overview**

This project investigates the detection of suicidal ideation in social media posts using an emoji-aware and multilingual deep learning framework.  
Social media language is informal, emotionally expressive, and often multilingual, making suicidality detection significantly more challenging than traditional sentiment analysis.

To address this, a hybrid transformer-based architecture is proposed that explicitly disentangles semantic intent and linguistic style and dynamically fuses them using a gated attention mechanism.  
The model is evaluated on English and Hindi text with a focus on safety-critical metrics such as recall and false negative rate.



---

## **Dataset**

### **Original Dataset**

- Dataset Name: **SuicidEmoji**
- Description: Social media posts annotated for suicidal ideation and enriched with emoji information.
- Source:  
  https://github.com/TianlinZhang668/SuicidEmoji
- Original Format:
  - `train.csv`
  - `val.csv`
  - `test.csv`
- License: **MIT License (2024, TianlinZhang668)**
- Note: The dataset was downloaded in its raw form (original version, without emoji removal or emoji name conversion).

---

### **Modified Dataset (This Project)**

To support multilingual and experimental analysis:

- Original CSV files were converted into XLSX files.
- Additional preprocessing and token-level transformations were applied.
- English and Hindi tokens were stored in the same dataset.
- The same processed dataset was used for both English and Hindi experiments.

**Example Files:**

- Original dataset (CSV)
- Processed dataset (XLSX)
- English and Hindi token representations

---

## **Preprocessing Pipeline**

The preprocessing pipeline was designed to preserve semantic and emotional information:

- Lowercasing and normalization  
- Emoji-to-text conversion (e.g., 😭 → `crying_face`)  
- URL and user mention removal  
- Tokenization and stopword removal (with negation preservation)  
- Lemmatization  
- Token-level English → Hindi translation  
- Preservation of emoji tokens during translation  

Preprocessing and translation scripts were implemented separately from the model training notebooks.

---

## **Model Architecture**

The proposed architecture consists of:

### **1) Semantic Encoder**

- Model: Twitter-XLM-RoBERTa  
- Role: Capture semantic intent and emotional meaning  
- Training: Fine-tuned  

### **2) Linguistic Encoder**

- English: XLM-RoBERTa  
- Hindi: MuRIL  
- Role: Capture structural and stylistic linguistic features  
- Training: Frozen during fine-tuning  

### **3) Handcrafted Linguistic Features**

Examples:

- Negation presence  
- Punctuation usage  
- Repetition ratio  
- Code-mixing indicators  

### **4) Hybrid Gated Attention (HGA)**

A learnable gating mechanism dynamically fuses results from semantic and linguistic representations.

### **5) Soft Disentanglement Loss (SDL)**

Encourages separation between semantic and linguistic representations to reduce feature overlap.

---

## **Experimental Setup**

- Platform: Google Colab  
- GPU: NVIDIA T4  
- Optimizer: AdamW  
- Learning Rate: 2 × 10⁻⁵  
- Batch Size: 8  
- Max Sequence Length: 160  
- Threshold Optimization: Youden’s J statistic  

Separate experiments were conducted for English and Hindi inputs using the same architecture.

---

## **Results**

### **Performance on the SuicidEmoji Dataset**

### **English Tokens**

| Metric      | Score  |
|-----------|--------|
| Accuracy  | 0.9058 |
| Precision | 0.7000 |
| Recall    | 0.8800 |
| F1-score  | 0.7797 |
| F2-score  | 0.8370 |
| FNR       | 0.1200 |
| MCC       | 0.7285 |
| AUC-ROC   | 0.9549 |
| AUC-PR    | 0.8529 |

---

### **Hindi Tokens**

| Metric      | Score  |
|-----------|--------|
| Accuracy  | 0.8896 |
| Precision | 0.6667 |
| Recall    | 0.8343 |
| F1-score  | 0.7411 |
| F2-score  | 0.7943 |
| FNR       | 0.1657 |
| MCC       | 0.6789 |
| AUC-ROC   | 0.9258 |
| AUC-PR    | 0.7882 |

The model achieves strong performance in both languages, demonstrating cross-lingual robustness and effectiveness of emoji-aware modeling.

---

## **Interpretability**

To ensure transparency in a safety-critical domain, multiple explainability techniques were applied:

- LIME explanations  
- Gate weight analysis  
- Representation probing  
- Saliency-based token masking  

Results show that emoji-derived tokens and semantic cues significantly influence suicidal predictions, while negations and neutral phrases often suppress risk scores.

---

## **Repository Structure**

├── notebooks/
│ ├── english_model.ipynb
│ ├── hindi_model.ipynb
│
├── data/
│ ├── original_samples/
│ ├── processed_samples/
│
├── scripts/
│ ├── preprocessing.py
│ ├── translation.py
│
├── results/
│ ├── metrics.txt
│ ├── plots/
│
└── README.md


---

## **Ethical Note**

This project deals with sensitive mental health data.  
The dataset is used strictly for research purposes.  
No attempt is made to identify individuals or deploy the model in real-world clinical settings.

---

## **License**

The original dataset is released under the MIT License by TianlinZhang668.  
This project follows the same licensing principles for research and educational use.

---

## **Future Work**

- Extend to code-mixed Hindi–English text.  
- Incorporate multimodal signals (images, memes).  
- Evaluate the model on real-time social media streams.  
- Improve interpretability and fairness in mental health AI systems.  
