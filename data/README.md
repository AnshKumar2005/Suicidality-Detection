The original dataset was already partitioned into training, validation, and test sets at the source.  
Each split was independently preprocessed and tokenized in this project, codes for which can be found in folder scripts.  
Token-level translation was applied to construct multilingual representations, and the processed data were stored in XLSX format.  
Each XLSX file contains both English and Hindi token representations within a unified structure, enabling consistent multilingual experimentation.
 
## Dataset Statistics
The distribution of suicidal and non-suicidal samples, along with emoji counts, is shown below:

| Category              | Train | Validation | Test |
|----------------------|-------|----------|------|
| Total cases          | 8628  | 1849     | 1848 |
| Total suicidal       | 1630  | 349      | 350  |
| Total non-suicidal   | 6998  | 1500     | 1498 |
| Total emojis         | 114118| 7863     | 5745 |

