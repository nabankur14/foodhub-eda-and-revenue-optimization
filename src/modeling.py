import pandas as pd
import numpy as np

def calculate_delivery_efficiency(df):
    """
    Calculates average delivery and preparation times.
    """
    avg_prep_time = df['food_preparation_time'].mean()
    avg_delivery_time = df['delivery_time'].mean()
    
    return {
        "avg_prep_time": avg_prep_time,
        "avg_delivery_time": avg_delivery_time
    }

def analyze_revenue(df):
    """
    Analyzes revenue generation.
    """
    total_revenue = df['cost_of_the_order'].sum()
    avg_order_value = df['cost_of_the_order'].mean()
    
    return {
        "total_revenue": total_revenue,
        "avg_order_value": avg_order_value
    }

def get_top_restaurants(df, n=5):
    """
    Returns the top n restaurants by order count.
    """
    return df['restaurant_name'].value_counts().head(n)

if __name__ == "__main__":
    # Test functions with processed data
    try:
        df = pd.read_csv("../data/processed/foodhub_order_processed.csv")
        print("Efficiency:", calculate_delivery_efficiency(df))
        print("Revenue:", analyze_revenue(df))
        print("Top Restaurants:\n", get_top_restaurants(df))
    except FileNotFoundError:
        print("Processed data not found. Run data_preprocessing.py first.")
