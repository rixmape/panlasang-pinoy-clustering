# Association Analysis of Filipino Cuisine Ingredients

This project uses association analysis to discover relationships between ingredients used in Filipino dishes. Apriori algorithm is used to mine frequent itemsets and association rules from a dataset of Filipino recipes.

## Project Structure

```plaintext
.
├── data
│   ├── preprocess_input
│   │   ├── stopwords.txt
│   │   ├── thesaurus.json
│   │   └── components.json
│   ├── preprocess_output
│   │   ├── 0_raw.txt
│   │   ├── 1_cleaned.txt
│   │   ├── 2_lemmatized.txt
│   │   ├── 3_filtered.txt
│   │   ├── 4_standardized_words.txt
│   │   ├── 5_unique.txt
│   │   ├── 6_standardized_phrase.txt
│   │   ├── 7_components.txt
│   │   ├── 8_filtered_common.txt
│   │   └── 9_filtered_unique.txt
│   ├── recipes
│   │   ├── all_recipes.json
│   │   ├── kawaling_pinoy.json
│   │   ├── maggi.json
│   │   ├── panlasang_pinoy.json
│   │   └── pinoy_cooking_recipes.json
│   ├── association_rules.json
│   ├── one_hot_encoded_recipes.json
│   └── preprocessed_recipes.json
...
```

- **data/preprocess_input**: Contains the files used for preprocessing the recipes.
- **data/preprocess_output**: Contains the output files of the preprocessing steps.
- **data/recipes**: Contains the raw recipe data from different sources.
- **data/association_rules.json**: Contains the association rules generated from the recipes.
- **data/one_hot_encoded_recipes.json**: Contains the recipes with one-hot encoded ingredients.
- **data/preprocessed_recipes.json**: Contains the preprocessed recipes from all sources.

## Data Preprocessing

The data preprocessing steps are as follows:

1. **Cleaning**: Remove special characters, numbers, and extra spaces.
2. **Lemmatization**: Convert words to their base form.
3. **Filtering**: Remove stopwords.
4. **Standardizing Words**: Standardize ingredients at the word level.
5. **Unique Ingredients**: Remove duplicate terms.
6. **Standardizing Phrases**: Standardize ingredients at the phrase level.
7. **Extracting Components**: Extract components from compound ingredients.
8. **Filtering Common Ingredients**: Remove common ingredients like water, salt, and pepper.
9. **Filtering Unique Ingredients**: Remove ingredients that appear in only one recipe.

## Installation

1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the main Jupyter Notebook `main.ipynb`.

## Suggested Improvements

This repository is now in public archive. Here are some suggestions for future improvements:

1. Consider other recipe websites that feature regional Filipino dishes.
2. Refine preprocessing to avoid unintentional removal of key ingredients.
3. Explore other algorithms for generating frequent itemsets other than Apriori.
4. Do a grid search to find the best hyperparameters.
5. Use the association rules to recommend ingredient substitutions or additions.
