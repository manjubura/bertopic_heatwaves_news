import pandas as pd
import ast

def load_data(country):
    """
    Load and preprocess data for a given country to extract specific columns.
    
    Parameters:
        country (str): The country name to load data for, as specified in the file name.
        
    Returns:
        dict: Dictionary containing extracted 'body', 'title', 'source', 'date' as lists.
    """
    
  # Define the file path based on the country
    file_path = f"data/all_{country.lower()}.xlsx"
    
    # Load the Excel file
    df = pd.read_excel(file_path)
    
    data = {
        f"{country.lower()}body": df['body'],
        f"{country.lower()}title": df['title'],
        f"{country.lower()}date": df['date'],  
        f"{country.lower()}source": df['source'].apply(lambda x: ast.literal_eval(x)['title'])
    }
    
    return data
