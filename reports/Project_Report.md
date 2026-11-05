# RetailPulse Project Report

## 1. Introduction
RetailPulse is a retail analytics prototype built using the Zidio Online Retail dataset. It combines transaction cleaning, customer segmentation, recency-based churn risk assessment and short-horizon demand forecasting.

## 2. Problem Statement
Retail businesses need to understand customer purchasing behavior and anticipate near-term demand to support retention and inventory decisions.

## 3. Objectives
- Prepare reliable transaction-level data.
- Measure customer recency, frequency and monetary value.
- Group customers into actionable segments.
- Highlight customers with long purchase gaps.
- Forecast daily sales for the next 30 days.

## 4. Technology
Python, Pandas, NumPy, Scikit-learn, Streamlit, Plotly and Joblib.

## 5. Data Preparation
The original file contains 536,640 rows. Exact duplicates were removed. Records missing CustomerID and rows with non-positive quantity/price or cancellation invoice IDs were excluded from customer-level sales modeling. The resulting modeling dataset contains 166,363 rows.

## 6. Results
- Customers analyzed: 2,997
- Countries represented: 33
- Products represented: 3,507
- Revenue in source currency: £3,865,463.08
- Analysis period: 2010-01-12 to 2011-12-10
- Forecast holdout MAE: 7,222.81
- Forecast holdout RMSE: 12,578.97

## 7. Machine Learning
K-Means with four clusters is used for customer segmentation after scaling and log-transforming skewed frequency and monetary values. Random Forest regression uses lagged daily sales and calendar features for forecasting.

## 8. Churn-Risk Limitation
No confirmed churn labels were supplied. Therefore, the prototype flags risk using recency thresholds (High: 180+ days; Medium: 90–179 days; Low: under 90 days). This is a rule-based proxy and must not be described as a validated supervised churn prediction.

## 9. Conclusion
RetailPulse transforms raw retail transactions into customer and sales insights. The prototype provides a reproducible data preparation pipeline, customer segments, a transparent recency-based risk indicator, and a baseline 30-day forecast. Future improvements include validating churn labels, adding inventory data, tuning models with time-series cross-validation, and deploying the dashboard to a public cloud service.
