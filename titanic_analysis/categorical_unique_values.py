import pandas as pd

def display_unique_values(df, categorical_features):
    unique_values = {}
    for i in categorical_features:
        unique_values[i] = df[i].unique().tolist()
    return unique_values

    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    
    