import streamlit as st
import pandas as pd
import os


def render_view_dataset():
    st.header("📂 View Dataset")

    # Adjust this path to your compressed parquet file
    dataset_path = "credit_card_dataset.parquet.zstd"

    if os.path.exists(dataset_path):
        try:
            # Load the Parquet file (compressed with Zstandard)
            df = pd.read_parquet(dataset_path, engine="pyarrow")

            # Count total records
            total_records = df.shape[0]

            # Show total records
            st.success("✅ Loaded dataset successfully.")
            st.write(f"📊 **Total Records:** {total_records}")

            # Show only the first 1000 rows
            st.dataframe(df.head(1000), use_container_width=True)
            st.caption("Showing only the first 1000 rows for performance.")

        except Exception as e:
            st.error(f"❌ Failed to read dataset: {e}")
    else:
        st.error(f"❌ File not found at: `{dataset_path}`")
