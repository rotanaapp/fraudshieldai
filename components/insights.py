import streamlit as st


def render_insights():
    st.markdown("### 🧠 AI-Generated Insights")
    st.info(
        """
- 🔁 **Repeat small transactions** observed before large fraudulent ones — often within short time windows.
- 🌍 **High fraud activity** from areas with **low population**, suggesting spoofed or rural IP usage.
- 👤 **Multiple fraudulent transactions** tied to **single card numbers**, indicating possible card testing or credential stuffing.
- 🏪 **Suspicious merchant patterns** in `grocery_pos` and `gas_transport` categories — commonly targeted for fraud.
- 📍 **Geographic mismatches** between user home location and merchant locations in fraud cases.
"""
    )
