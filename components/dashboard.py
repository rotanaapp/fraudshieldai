import streamlit as st
import pandas as pd
from components.alerts import render_alerts
from components.insights import render_insights


# Load and preprocess data efficiently
@st.cache_data(show_spinner="Loading dataset...")
def load_data():
    df = pd.read_parquet("credit_card_dataset.parquet.zstd", engine="pyarrow")

    # Convert datetime column if not already
    if not pd.api.types.is_datetime64_any_dtype(df["trans_date_trans_time"]):
        df["trans_date_trans_time"] = pd.to_datetime(df["trans_date_trans_time"])

    # Vectorized risk level assignment
    df["risk_level"] = pd.cut(
        df["amt"],
        bins=[-float("inf"), 0, 1000, 5000, float("inf")],
        labels=["None", "Low", "Medium", "High"],
    )

    return df


# Main dashboard function
def render_dashboard():
    st.markdown("## 📊 Fraud Detection Overview")

    # Load dataset
    df = load_data()

    # Get transaction date range
    min_date = df["trans_date_trans_time"].min().strftime("%b %d, %Y")
    max_date = df["trans_date_trans_time"].max().strftime("%b %d, %Y")
    st.caption(f"🗓️ **Transaction Date Range:** {min_date} – {max_date}")

    # Calculate metrics
    high_risk_count = (df["risk_level"] == "High").sum()
    medium_risk_count = (df["risk_level"] == "Medium").sum()
    fraud_amount = df[df["is_fraud"] == 1]["amt"].sum()
    fraud_amount_display = f"${fraud_amount / 1_000:,.0f}K"

    # Display metric cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🔴 High Risk Transactions", f"{high_risk_count:,}")
        st.caption("Transactions with the highest likelihood of fraud")

    with col2:
        st.metric("🟠 Medium Risk Transactions", f"{medium_risk_count:,}")
        st.caption("Moderately suspicious transactions")

    with col3:
        st.metric("💰 Fraudulent Amount", fraud_amount_display)
        st.caption("Total dollar amount of confirmed fraudulent activity")

    st.markdown("---")
    render_alerts()
    st.markdown("---")
    render_insights()
