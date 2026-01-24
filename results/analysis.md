# Detailed Model Analysis

This document presents a deeper analysis of the proposed hybrid transformer model, focusing on prediction confidence, representation disentanglement, and interpretability.

---

## 1. Confidence Stratification Analysis

Confidence stratification was performed by grouping predictions into probability bins and analyzing the distribution of true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN).

### Key Observations (English)

- False negatives are concentrated in low-confidence bins (< 0.40).
- True positives are predominantly observed in high-confidence bins (> 0.75).
- False positives mostly occur in mid-to-high confidence ranges.

### Key Observations (Hindi)

- True positives are strongly concentrated in high-confidence bins (> 0.75).
- False negatives are distributed across low and mid-confidence bins.
- The overall confidence distribution is consistent with the English dataset.

This indicates that the model assigns higher confidence to correctly identified suicidal posts, which is desirable in safety-critical applications.

---

## 2. Gate Weight Analysis

The hybrid gated attention mechanism dynamically balances semantic and linguistic representations.

### Insights

- Higher gate values were observed in suicidal predictions, indicating stronger reliance on semantic intent.
- Non-suicidal predictions showed relatively higher dependence on linguistic structure.
- This behavior validates the design objective of separating semantic meaning from linguistic style.

---

## 3. Representation Disentanglement

To evaluate semantic–linguistic separation, probing experiments were conducted.

### Probing Scores

| Language | Semantic Score | Linguistic Score |
|---------|--------------|-----------------|
| English | 0.943        | 0.854           |
| Hindi   | 0.907        | 0.652           |

### Interpretation

- Semantic representations capture suicidal intent more strongly than linguistic features.
- Lower linguistic probing scores in Hindi suggest greater semantic dominance in multilingual settings.
- These results confirm effective disentanglement between semantic and linguistic representations.

---

## 4. Interpretability Analysis (LIME)

LIME was used to analyze token-level contributions to model predictions.

### English Dataset

**Tokens supporting suicidal predictions:**

- suicidal, death, alive, anymore, end

**Tokens suppressing suicidal predictions:**

- week, ppl

### Hindi Dataset

**Tokens supporting suicidal predictions:**

- र, गय, अब, ज, वन

**Tokens suppressing suicidal predictions:**

- च, हर

### Key Insight

Emotionally salient words and emoji-derived tokens strongly influence suicidal predictions, while neutral or negation-related tokens suppress risk scores.

---

## 5. Error Analysis

### False Negatives (FN)

- Often occur in posts with implicit or metaphorical expressions of distress.
- Emojis sometimes convey ambiguous emotional signals that reduce model confidence.

### False Positives (FP)

- Frequently arise in emotionally intense but non-suicidal posts.
- Linguistic exaggeration and sarcasm contribute to misclassification.

These findings highlight the inherent difficulty of distinguishing emotional expression from genuine suicidal intent in social media text.
