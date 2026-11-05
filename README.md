# RetailPulse – AI-Powered Customer Analytics & Demand Forecasting Platform

## Overview
RetailPulse analyzes online retail transactions to understand customer value, segment customers, flag recency-based churn risk, and generate a 30-day baseline sales forecast.

## Dataset
Provided Zidio files:
- `Online_Retail.csv` – transaction-level retail data
- `customer_rfm_features.csv.xls` – supplied customer RFM features
- `daily_rolling_statistics_fixed.csv` – supplied daily rolling statistics

## Project results
- Raw transaction rows: 536,640
- Valid cleaned transaction rows: 166,363
- Customers retained: 2,997
- Countries: 33
- Products: 3,507
- Revenue: £3,865,463.08
- Period: 2010-01-12 to 2011-12-10

## Run locally
```bash
pip install -r requirements.txt
streamlit run dashboard/app.py
```

## Methodology
1. Remove exact duplicate rows.
2. Exclude rows without CustomerID and invalid/cancelled/negative sales from customer-level sales modeling.
3. Calculate Revenue = Quantity × UnitPrice.
4. Recalculate RFM features from cleaned transactions.
5. Apply K-Means customer segmentation.
6. Create a transparent recency-based churn-risk proxy.
7. Train a Random Forest baseline on lagged daily sales and produce a 30-day forecast.

## Important limitations
The supplied dataset has no verified churn outcome labels, so churn output is a rule-based risk proxy, not a supervised churn probability. Forecasting is a baseline trained on a short historical period and should be validated further before business use. Currency values follow the source dataset's unit (commonly GBP).

## Structure
- `data/raw/` – original Zidio datasets
- `data/processed/` – cleaned and engineered datasets
- `src/` – modeling pipeline
- `dashboard/` – Streamlit application
- `models/` – saved model artifacts
- `reports/` – metrics and validation outputs
