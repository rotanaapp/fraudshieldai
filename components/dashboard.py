import streamlit as st
import matplotlib.pyplot as plt
from components.alerts import render_alerts
from components.insights import render_insights


def render_risk_pie():
    labels = ["High", "Medium", "Low", "None"]
    sizes = [24, 32, 28, 16]
    colors = ["#EF553B", "#FFA15A", "#00CC96", "#AB63FA"]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140)
    ax.axis("equal")
    st.pyplot(fig)


def render_dashboard():
    st.markdown("## 📊 Fraud Detection Overview")
    st.caption("Mar 1, 2025 – Mar 31, 2025")

    # Top Metrics Cards
    col1, col2, col3 = st.columns(3)
    col1.metric("🔴 High Risk Transactions", "87", "+12%")
    col2.metric("🟠 Medium Risk Transactions", "142", "-3%")
    col3.metric("🟢 Prevented Fraud Amount", "$285K", "+18%")

    st.markdown("---")

    main_col, side_col = st.columns([3, 2])

    with main_col:
        # st.markdown("### 📈 Summary Visuals (placeholder)")
        render_risk_pie()
        # render_alerts()

    with side_col:
        render_insights()

    st.markdown("---")
    render_alerts()
