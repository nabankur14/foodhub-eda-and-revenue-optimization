# FoodHub EDA and Revenue Optimization

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

**A data-driven analysis to optimize revenue and operational efficiency for a food aggregator platform.**

## Table of Contents
- [Project Overview](#project-overview)
- [Business Problem](#business-problem)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Key Results](#key-results)
- [Business Impact](#business-impact)
- [Skills](#skills)
- [Key Learnings](#key-learnings)
- [Repository Structure](#repository-structure)
- [How to Run](#how-to-run)
- [Future Improvements](#future-improvements)
- [Author](#author)

## Project Overview
This project analyzes customer orders from FoodHub, a New York-based food aggregator app. The comprehensive analysis uncovers patterns in customer demand, cuisine preferences, and delivery efficiency to drive revenue growth and improve user experience.

## Business Problem
**Context**: In the competitive NYC food delivery market, understanding customer behavior and operational bottlenecks is crucial.
**Stakeholders**: Business Strategy Team, Operations Managers, Marketing Team.
**Decision Impact**:
- Optimize delivery logistics to reduce wait times.
- Tailor marketing campaigns based on cuisine popularity.
- Identify underperforming areas to boost customer retention.

## Dataset
- **Source**: Kaggle / FoodHub proprietary data.
- **Size**: 1898 records, 9 features.
- **Key Features**:
    - `order_id`, `customer_id`, `restaurant_name`
    - `cuisine_type`, `cost_of_the_order`
    - `day_of_the_week`, `rating`
    - `food_preparation_time`, `delivery_time`
- **Data Types**: Mixed (Numerical and Categorical).

## Methodology
1.  **Data Cleaning**: Handled missing rating values and validated data types.
2.  **Exploratory Data Analysis (EDA)**:
    -   Univariate analysis of costs, timings, and ratings.
    -   Bivariate analysis to find correlations (e.g., Cost vs. Day of Week).
3.  **Feature Engineering**: Derived metrics for total order time and revenue categorization.
4.  **Evaluation**: Assessed customer satisfaction through rating distributions.

## Key Results
-   **Top Cuisine**: American, Japanese, and Italian cuisines drive the majority of orders.
-   **Revenue**: The average order value is consistent, but weekends see a significant spike in volume.
-   **Efficiency**: Average delivery time is ~24 minutes, while prep time is ~27 minutes.
-   **Satisfaction**: A significant portion (approx 38%) of orders are unrated, presenting a feedback gap.

## Business Impact
1.  **Promotional Strategy**: Focus marketing spend on American and Japanese cuisines during weekends to maximize high-volume periods.
2.  **Operational Fix**: Investigate restaurants with high prep times to reduce overall wait duration below 50 minutes.
3.  **Feedback Loop**: Implement a post-order incentive (e.g., small discount) to encourage customers to leave ratings, reducing the 'Not given' category.

## Skills
**Technical Skills**
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/-Seaborn-7db9e8?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/-Jupyter-F37626?logo=jupyter&logoColor=white)

**Soft Skills**
![Analytical Thinking](https://img.shields.io/badge/-Analytical_Thinking-lightgrey)
![Communication](https://img.shields.io/badge/-Communication-lightgrey)
![Problem Solving](https://img.shields.io/badge/-Problem_Solving-lightgrey)

## Key Learnings
-   Real-world data often has gaps (e.g., missing ratings) that require strategic handling rather than simple deletion.
-   Operational metrics (prep time) are just as critical as financial metrics (counts) for platform success.
-   Visual storytelling is essential to convey technical findings to business stakeholders.

## Repository Structure
```
foodhub-eda-and-revenue-optimization/
│
├── data/
│   ├── raw/                  # Original dataset
│   └── processed/            # Cleaned data
│
├── notebooks/
│   ├── analysis.ipynb        # Cleaned notebook
│   └── original_analysis.ipynb    # Full original notebook
│
├── src/                      # Source code
│   ├── data_preprocessing.py
│   ├── modeling.py
│   └── evaluation.py
│
├── visuals/
│   └── charts/               # Exported plots
│
├── requirements.txt
└── README.md
```

### Visuals from the Project
Below are selected visuals from the project analysis.

![Order Cost](../visuals/charts/order_cost_distribution.png)
*Distribution of order costs showing prevalent spending habits.*

![Top Restaurants](../visuals/charts/top_restaurants.png)
*Top 10 performing restaurants on the platform.*

## How to Run
1.  **Clone the repository**:
    ```bash
    git clone <repo-url>
    cd foodhub-eda-and-revenue-optimization
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the notebook**:
    ```bash
    jupyter notebook notebooks/analysis.ipynb
    ```

## Future Improvements
1.  **Predictive Modeling**: Implement regression to predict delivery time based on day and restaurant.
2.  **Sentiment Analysis**: If text reviews become available, analyze sentiment to correlate with ratings.
3.  **Dashboarding**: Create an interactive Streamlit dashboard for real-time monitoring.

## Author
**Nabankur Ray**
*Data Scientist | Business Analyst | Machine Learning Engineer*

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/nabankur14)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/nabankur-ray)
