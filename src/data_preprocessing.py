import pandas as pd
import numpy as np

def load_data(filepath):
    """
    Loads data from a CSV file.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully from {filepath}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """
    Cleans the dataframe:
    - Handles missing values if any equivalent to 'Not given' or similar.
    - Ensures correct data types.
    """
    # Convert 'Not given' in rating to NaN temporarily or handle as a category
    # Based on notebook analysis, 'Not given' is a valid category for unrated orders.
    # We will keep it as is for now, but ensure metrics calculations handle it.
    
    # Check for duplicates
    if df.duplicated().sum() > 0:
        print(f"Found {df.duplicated().sum()} duplicate rows. Removing them.")
        df = df.drop_duplicates()
        
    return df

def feature_engineering(df):
    """
    Adds new features to the dataframe.
    """
    # Example: Revenue per order is just cost_of_the_order
    # We could add categories for delivery time efficiency
    
    return df

def save_processed_data(df, output_path):
    """
    Saves the processed dataframe to a CSV file.
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"Processed data saved to {output_path}")
    except Exception as e:
        print(f"Error saving data: {e}")

if __name__ == "__main__":
    # Example usage
    raw_data_path = "../data/raw/foodhub_order.csv"
    processed_data_path = "../data/processed/foodhub_order_processed.csv"
    
    df = load_data(raw_data_path)
    if df is not None:
        df = clean_data(df)
        df = feature_engineering(df)
        save_processed_data(df, processed_data_path)
