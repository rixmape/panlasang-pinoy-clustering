# Ingredient-Based Clustering of Filipino Dishes

## Overview

This project aims to identify clusters of Filipino dishes based on their ingredients, utilizing data mining, natural language processing (NLP), and unsupervised learning techniques. By analyzing a dataset of Filipino recipes, we extract common ingredients to define a unique Filipino pantry and discover patterns in Filipino cuisine.

## Project Structure

- `main.ipynb`: Jupyter notebook containing the main analysis, data processing, clustering, and visualization steps.
- `scrape-recipes.py`: Python script for scraping Filipino recipes from various online sources to create the dataset.
- `./data/`: Directory containing the dataset and various processed data files.
  - `cleaned_ingredients.txt`: List of unique ingredients after preprocessing.
  - `cleaned_recipes.json`: JSON file with recipes and their cleaned ingredients.
  - `culinary_stopwords.txt`: List of stopwords specific to culinary terms.
  - `phrase_synonyms.json`: JSON file mapping ingredient phrase synonyms to a common name.
  - `rare_ingredients.txt`: List of ingredients filtered out due to rarity.
  - `recipes/`: Folder containing the raw recipe data in JSON format.
  - `word_synonyms.json`: JSON file mapping ingredient word synonyms to a common name.
- `LICENSE`: The license file for the project.
- `README.md`: This file, providing an overview and instructions for the project.

## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook or JupyterLab
- Libraries: `pandas`, `plotly`, `scikit-learn`, `spacy`, `sentence_transformers`, `matplotlib`, `seaborn`
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository to your local machine.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install the required libraries: `pip install -r requirements.txt`
5. Download the necessary Spacy model: `python -m spacy download en_core_web_lg`

### Running the Notebook

- Launch Jupyter Notebook or JupyterLab in the project directory.
- Open `main.ipynb` and run the cells sequentially to perform the analysis.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
