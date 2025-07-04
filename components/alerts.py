import streamlit as st
from utils.data import recent_alerts


def color_risk(val):
    risk = int(val.strip("%"))
    if risk > 95:
        return "background-color: #FF4C4C; color: white"
    elif risk > 90:
        return "background-color: #FFA07A"
    else:
        return ""


def render_alerts():
    st.markdown("### 📋 Recent High-Risk Alerts")
    styled_alerts = recent_alerts.style.applymap(color_risk, subset=["Risk Score"])
    st.dataframe(styled_alerts, use_container_width=True)
