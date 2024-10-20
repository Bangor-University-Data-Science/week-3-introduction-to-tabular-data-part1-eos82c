import pandas as pd 

def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    return pd.DataFrame({"Feature": df.columns, "Data Type": df.dtypes, "Numer of Unique Values": df.nunique(), "Missing Values": df.isnll().any()})




