import pandas as pd
import streamlit as st


def color_risk(val):
    risk = float(val.strip("%"))
    if risk > 95:
        return "background-color: #FF4C4C; color: white"
    elif risk > 90:
        return "background-color: #FFA07A"
    else:
        return ""


def render_alerts():
    st.markdown("### 📋 Recent High-Risk Alerts")

    # Load dataset
    df = pd.read_parquet("credit_card_dataset.parquet.zstd", engine="pyarrow")

    # Create risk_score from amt
    max_amt = df["amt"].max()
    df["risk_score"] = (df["amt"] / max_amt) * 100

    # Filter high-risk alerts
    recent_alerts = df[df["risk_score"] > 90].copy()

    # Format risk score
    recent_alerts["Risk Score"] = recent_alerts["risk_score"].round(1).astype(str) + "%"

    # Select columns including customer info
    show_cols = [
        "trans_date_trans_time",
        "first",
        "last",
        "gender",
        "merchant",
        "category",
        "amt",
        "risk_score",
        "Risk Score",
    ]
    alerts_to_show = (
        recent_alerts[show_cols].sort_values("risk_score", ascending=False).head(20)
    )

    # Style Risk Score
    styled_alerts = alerts_to_show.style.applymap(color_risk, subset=["Risk Score"])
    st.dataframe(styled_alerts, use_container_width=True)
