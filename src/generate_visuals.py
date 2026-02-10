import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Ensure directories exist
os.makedirs('../visuals/charts', exist_ok=True)

# Load Data
try:
    df = pd.read_csv('../data/raw/foodhub_order.csv')
except FileNotFoundError:
    print("Data file not found. Please check data/raw/foodhub_order.csv")
    sys.exit(1)

# 1. Order Cost Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='cost_of_the_order', kde=True)
plt.title('Distribution of Order Cost')
plt.xlabel('Cost ($)')
plt.ylabel('Frequency')
plt.savefig('../visuals/charts/order_cost_distribution.png')
plt.close()
print("Saved order_cost_distribution.png")

# 2. Rating Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='rating', order=['3', '4', '5', 'Not given'])
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.savefig('../visuals/charts/rating_distribution.png')
plt.close()
print("Saved rating_distribution.png")

# 3. Top 10 Restaurants
top_restaurants = df['restaurant_name'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_restaurants.values, y=top_restaurants.index)
plt.title('Top 10 Restaurants by Order Count')
plt.xlabel('Number of Orders')
plt.ylabel('Restaurant Name')
plt.savefig('../visuals/charts/top_restaurants.png')
plt.close()
print("Saved top_restaurants.png")

# 4. Cuisine Type Distribution
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='cuisine_type', order=df['cuisine_type'].value_counts().index)
plt.title('Cuisine Type Distribution')
plt.xlabel('Cuisine Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.savefig('../visuals/charts/cuisine_distribution.png')
plt.close()
print("Saved cuisine_distribution.png")
