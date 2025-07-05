import streamlit as st
from components.dashboard import render_dashboard
from components.check_txns import render_check_txns
from components.view_dataset import render_view_dataset


def render_sidebar():
    st.sidebar.title("🛡️ Fraud Shield AI")
    page = st.sidebar.radio(
        "Menu", ["📊 Dashboard", "💳 Check TXNs", "📂 View Dataset"]
    )

    if page == "📊 Dashboard":
        render_dashboard()
    elif page == "💳 Check TXNs":
        render_check_txns()
    elif page == "📂 View Dataset":
        render_view_dataset()

    st.sidebar.markdown("---")
    st.sidebar.info("**Group II**  \nMSIT Y2T1 B9-Aritificial Intelligence")
    return page
