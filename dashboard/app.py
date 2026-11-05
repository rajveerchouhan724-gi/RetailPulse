import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/"data"/"processed"
st.set_page_config(page_title="RetailPulse",layout="wide")
st.title("RetailPulse | Customer Analytics & Demand Forecasting")
st.caption("Retail transaction intelligence dashboard")
tx=pd.read_csv(D/"cleaned_transactions.csv",parse_dates=["InvoiceDate"])
rfm=pd.read_csv(D/"customer_segments.csv")
risk=pd.read_csv(D/"customer_churn_risk_proxy.csv")
fc=pd.read_csv(D/"demand_forecast_30_days.csv",parse_dates=["Date"])
a,b,c,d=st.columns(4)
a.metric("Net Revenue",f"£{tx.Revenue.sum():,.0f}")
b.metric("Customers",f"{tx.CustomerID.nunique():,}")
c.metric("Orders",f"{tx.InvoiceNo.nunique():,}")
d.metric("Products",f"{tx.StockCode.nunique():,}")
st.subheader("Daily Revenue Trend")
daily=tx.assign(Date=tx.InvoiceDate.dt.date).groupby("Date",as_index=False).Revenue.sum()
st.plotly_chart(px.line(daily,x="Date",y="Revenue",title="Daily Revenue"),use_container_width=True)
left,right=st.columns(2)
with left:
    st.subheader("Customer Segments")
    seg=rfm.Segment.value_counts().rename_axis("Segment").reset_index(name="Customers")
    st.plotly_chart(px.bar(seg,x="Segment",y="Customers"),use_container_width=True)
with right:
    st.subheader("Churn Risk (recency-based proxy)")
    cr=risk.ChurnRisk.value_counts().rename_axis("Risk").reset_index(name="Customers")
    st.plotly_chart(px.pie(cr,names="Risk",values="Customers"),use_container_width=True)
st.subheader("Next 30-Day Demand Forecast")
st.plotly_chart(px.line(fc,x="Date",y="ForecastSales",markers=True),use_container_width=True)
st.info("Churn risk is a rule-based recency proxy because the supplied data has no confirmed churn labels. Forecasts are baseline model estimates, not guaranteed outcomes.")
st.subheader("Customer Details")
st.dataframe(rfm.head(100),use_container_width=True)
