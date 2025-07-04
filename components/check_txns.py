import streamlit as st
import pandas as pd
from utils.model import load_model_and_encoder
from utils.distance import haversine


def render_check_txns():
    st.markdown("## 🧾 Check Transaction for Fraud")
    st.markdown(
        "Fill in the transaction details below to verify whether it's fraudulent."
    )

    model, encoder = load_model_and_encoder()

    with st.form("fraud_form", border=True):
        st.markdown("### 🔧 Transaction Inputs")

        col1, col2 = st.columns(2)

        with col1:
            merchant = st.text_input("🛍️ Merchant Name")
            category = st.text_input("📂 Transaction Category")
            amt = st.number_input(
                "💵 Transaction Amount ($)", min_value=0.0, format="%.2f"
            )
            lat = st.number_input("📍 Cardholder Latitude", format="%.6f")
            long = st.number_input("📍 Cardholder Longitude", format="%.6f")
            merch_lat = st.number_input("🏬 Merchant Latitude", format="%.6f")
            merch_long = st.number_input("🏬 Merchant Longitude", format="%.6f")

        with col2:
            gender = st.selectbox("👤 Gender", ["Male", "Female"])
            cc_num = st.text_input("💳 Credit Card Number")
            hour = st.slider("⏱️ Transaction Hour", 0, 23, 12)
            day = st.slider("📅 Day of Month", 1, 31, 15)
            month = st.slider("🗓️ Month", 1, 12, 6)

        submitted = st.form_submit_button("🔍 Analyze Transaction")

    if submitted:
        if merchant and category and cc_num:
            distance = haversine(lat, long, merch_lat, merch_long)
            df = pd.DataFrame(
                [[merchant, category, amt, distance, hour, day, month, gender, cc_num]],
                columns=[
                    "merchant",
                    "category",
                    "amt",
                    "distance",
                    "hour",
                    "day",
                    "month",
                    "gender",
                    "cc_num",
                ],
            )

            # Encode categorical values
            for col in ["merchant", "category", "gender"]:
                try:
                    df[col] = encoder[col].transform(df[col])
                except:
                    df[col] = -1  # Unknown category fallback

            df["cc_num"] = df["cc_num"].apply(lambda x: hash(x) % 100)

            # Make prediction
            prediction = model.predict(df)[0]

            # Display prediction result in a styled box
            with st.container(border=True):
                st.markdown("### 🧾 Prediction Result")
                if prediction == 1:
                    st.error("🚨 **Fraudulent Transaction Detected!**", icon="⚠️")
                else:
                    st.success("✅ **Legitimate Transaction**", icon="✔️")
        else:
            st.warning("⚠️ Please fill out all required fields.")
