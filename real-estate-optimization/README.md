# Real Estate Price Optimization Model

## Overview
This project implements a data-driven pricing engine designed to estimate fair market value for residential real estate. By leveraging Machine Learning techniques on aggregated listing data, the system identifies pricing inefficiencies and potential investment opportunities in high-density urban markets.

## Methodology

### 1. Data Acquisition & Pipeline
The system utilizes a custom scraping pipeline to aggregate housing data from major real estate platforms.
* **Target Metrics:** List price, square footage, bedroom/bathroom count, lot size, year built, and location coordinates.
* **Preprocessing:** The pipeline handles data cleaning, including outlier removal (Z-score filtering), missing value imputation, and categorical encoding of neighborhood features.

### 2. Feature Engineering
To improve predictive accuracy, the model incorporates derived features:
* **Geospatial Clustering:** Uses latitude/longitude data to group properties into micro-neighborhoods, capturing location-specific value premiums.
* **Price-to-Rent Ratios:** Estimates yield potential based on local rental market data.
* **Seasonality Adjustments:** Normalizes prices based on historical time-on-market trends.

### 3. Machine Learning Architecture
* **Algorithm:** Random Forest Regressor. This ensemble method is selected for its ability to handle non-linear relationships between property features (e.g., diminishing returns on square footage) and its robustness against overfitting.
* **Validation:** The model is evaluated using K-Fold Cross Validation, optimizing for Mean Absolute Error (MAE) to ensure pricing estimates remain within a actionable margin of error.

## Key Insights
The model analysis highlights that while square footage provides the baseline for valuation, neighborhood clustering and "year since renovation" are the strongest predictors of price variance above the median.

