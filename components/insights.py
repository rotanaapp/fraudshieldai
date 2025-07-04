import streamlit as st


def render_insights():
    st.markdown("### 🧠 AI-Generated Insights")
    st.info(
        """
- **Multiple small transactions** from foreign IPs followed by one large one.
- **Account takeovers** using credential stuffing from Eastern Europe.
- **Synthetic identities** spike detected in new account registrations.
"""
    )
