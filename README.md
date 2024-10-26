# Project overview

This project employs topic modelling using BERTopic to analyse heatwave news articles from online news sources from five countries (India, Nepal, Mexico, UK, and US). Outputs from BERTopic are used for grounded theory analysis of narratives and framing of heatwave news. 

# File descriptions

* `config.yaml`: A configuration file that stores hyperparameters for each country's BERTopic model.
* `main_script.py`: Main script that loads configurations, handles preprocessing and runs BERTopic models for each country.
* `model/`: Directory where country specific model is saved.
* `utils/preprocess.py`: Contains helper functions for data loading and preprocessing for country specific preprocessing steps.
* `requirements.txt`: Lists required Python libraries and packages for the project.

# Preprocessing variations

Different preprocessing steps were applied based on country-specific characteristics. These variations are documented in config.yaml and implemented in preprocess.py. 
* India: Hinglish stopwords were removed
* Nepal: Nepali stopwords were removed
* --- finish ---

_These preprocessing steps were taken to ensure that stopwords and special characters were processed properly by the model, especially given the language and that they were avoided to be there as representative terms_

# Setup 

1. Install dependencies.
   
Install required libraries by running:

```
pip install -r requirements.txt
```

2. Data access.

News data is in the `data/` directory where each file is an excel file specific to each country, named according to the country code.

- `all_in.xlsx` - News data for India  
- `all_np.xlsx` - News data for Nepal
- `all_mex.xlsx` - News data for Mexico
- `all_uk.xlsx` - News data for UK
- `all_us.xlsx` - News data for US

3. Run the code.

Run the `main_script.py` to train BERTopic models for each country.

```
python main_script.py
```

