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
│   │   └── 7_components.txt
│   ├── recipes
│   │   ├── all_recipes.json
│   │   ├── kawaling_pinoy.json
│   │   ├── maggi.json
│   │   ├── panlasang_pinoy.json
│   │   └── pinoy_cooking_recipes.json
│   └── preprocessed_recipes.json
...
```

- **data/preprocess_input**: Contains the files used for preprocessing the recipes.
- **data/preprocess_output**: Contains the output files of the preprocessing steps.
- **data/recipes**: Contains the raw recipe data from different sources.
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

## Installation

1. Clone the repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the main Jupyter Notebook `main.ipynb`.

## How to Contribute

### Improving the Preprocessed Data

1. Stopwords
   1. Run `main.ipynb` until step 3 to get ingredient list without stopwords.
   2. Manually check the output file `data/preprocess_output/3_filtered.txt` for any remaining stopwords.
   3. Add the stopwords to `data/preprocess_input/stopwords.txt`.
   4. Run step 3 again to remove the newly added stopwords.
2. Standard names
   1. Run steps 4 to 6 to get the standardized ingredient names.
   2. Manually check the output file `data/preprocess_output/6_standardized_phrase.txt` for any inconsistencies.
   3. Add the correct standard names to `data/preprocess_input/thesaurus.json`.
   4. Run steps 4 to 6 again to standardize the ingredients using the updated thesaurus.
3. Components
   1. Run step 7 to extract components from compound.
   2. Manually check the output file `data/preprocess_output/7_components.txt` for any compound ingredients that need to be split.
   3. Add the correct components to `data/preprocess_input/components.json`.
   4. Run step 7 again to extract the components using the updated components list.
4. Preprocessed recipes
   1. Run the entire notebook to preprocess the recipes using the updated stopwords, thesaurus, and components list.
   2. Manually check the output file `data/preprocessed_recipes.json` for any inconsistencies.
   3. Make the necessary changes to the preprocessing steps in the notebook.
