import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from components.alerts import render_alerts
from components.insights import render_insights


# Cached data loading from Parquet file
@st.cache_data(show_spinner="Loading dataset...")
def load_data():
    return pd.read_parquet("credit_card_dataset.parquet.zstd", engine="pyarrow")


# Assign risk levels based on amount
def get_risk_level(row):
    if row["amt"] >= 5000:
        return "High"
    elif row["amt"] >= 1000:
        return "Medium"
    elif row["amt"] > 0:
        return "Low"
    else:
        return "None"


# Main dashboard function
def render_dashboard():
    st.markdown("## 📊 Fraud Detection Overview")

    # Load dataset
    df = load_data()

    # Parse datetime column
    df["trans_date_trans_time"] = pd.to_datetime(df["trans_date_trans_time"])

    # Get min and max dates
    min_date = df["trans_date_trans_time"].min().strftime("%b %d, %Y")
    max_date = df["trans_date_trans_time"].max().strftime("%b %d, %Y")
    st.caption(f"{min_date} – {max_date}")

    # Derive risk level
    df["risk_level"] = df.apply(get_risk_level, axis=1)

    # Metrics
    high_risk_count = (df["risk_level"] == "High").sum()
    medium_risk_count = (df["risk_level"] == "Medium").sum()
    fraud_amount = df[df["is_fraud"] == 1]["amt"].sum()
    fraud_amount_display = f"${fraud_amount / 1_000:.0f}K"

    # Display metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("🔴 High Risk Transactions", f"{high_risk_count}")
    col2.metric("🟠 Medium Risk Transactions", f"{medium_risk_count}")
    col3.metric("🟢 Prevented Fraud Amount", fraud_amount_display)

    st.markdown("---")
    render_alerts()
    st.markdown("---")
    render_insights()
