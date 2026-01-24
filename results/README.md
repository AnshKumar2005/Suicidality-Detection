# Model Results

This section summarizes the performance and interpretability analysis of the proposed hybrid transformer model on English and Hindi datasets.

---

## 1. Overall Performance

The model demonstrates strong performance across both languages, with high recall and low false negative rates, which are critical for suicidality detection.

Key observations:

- English performance is slightly higher than Hindi.
- False negatives are significantly lower than false positives.
- The model shows robust cross-lingual generalization.

---

## 2. Confidence Stratification Analysis

Confidence stratification was performed to analyze prediction reliability across probability bins.

### English Dataset

- Most true positives occur in high-confidence bins (>0.75).
- False negatives are concentrated in low-confidence ranges (<0.40).
- False positives tend to appear in mid-to-high confidence ranges.

### Hindi Dataset

- True positives are predominantly observed in high-confidence bins (>0.75).
- False negatives are distributed across low and mid-confidence bins.
- False positives show a similar distribution pattern to English.

This analysis indicates that the model assigns higher confidence to correctly detected suicidal posts.

---

## 3. Representation Disentanglement

To validate semantic–linguistic separation, representation probing and visualization were performed.

### Semantic vs Linguistic Probing Scores

| Language | Semantic Score | Linguistic Score |
|---------|--------------|-----------------|
| English | 0.943        | 0.854           |
| Hindi   | 0.907        | 0.652           |

These results indicate that semantic representations capture suicidal intent more strongly than linguistic features, validating the disentanglement objective.

---

## 4. Interpretability Analysis (LIME)

LIME explanations were used to analyze model decision-making.

### English Dataset

- Tokens supporting suicidal prediction:
  - suicidal, death, alive, anymore, end
- Tokens suppressing suicidal prediction:
  - week, ppl

### Hindi Dataset

- Tokens supporting suicidal prediction:
  - र, गय, अब, ज, वन
- Tokens suppressing suicidal prediction:
  - च, हर

These findings highlight the role of emotionally salient words and emoji-derived tokens in suicidality detection.

---

## 5. Key Insights

- Emoji-aware modeling significantly improves intent detection.
- Semantic cues dominate suicidal predictions, while linguistic cues refine decision boundaries.
- The hybrid gated architecture enhances interpretability and robustness across languages.
