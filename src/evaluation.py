import pandas as pd

def evaluate_customer_satisfaction(df):
    """
    Evaluates customer satisfaction based on ratings.
    """
    # Filter out 'Not given' for numerical calculation if needed, 
    # or just count distribution.
    
    rated_orders = df[df['rating'] != 'Not given'].copy()
    rated_orders['rating'] = rated_orders['rating'].astype(int)
    
    avg_rating = rated_orders['rating'].mean()
    rating_counts = df['rating'].value_counts(normalize=True) * 100
    
    return {
        "average_rating": avg_rating,
        "rating_distribution": rating_counts
    }

def print_evaluation_report(metrics):
    """
    Prints a formatted report of the metrics.
    """
    print("--- Business Evaluation Report ---")
    print(f"Average Customer Rating: {metrics['average_rating']:.2f}/5.0")
    print("\nRating Distribution (%):")
    print(metrics['rating_distribution'])

if __name__ == "__main__":
    try:
        df = pd.read_csv("../data/processed/foodhub_order_processed.csv")
        metrics = evaluate_customer_satisfaction(df)
        print_evaluation_report(metrics)
    except FileNotFoundError:
        print("Processed data not found. Run data_preprocessing.py first.")
