# import streamlit as st
# import pandas as pd
# import os


# def render_view_dataset():
#     st.header("📂 View Dataset")

#     uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

#     if uploaded_file is not None:
#         df = pd.read_csv(uploaded_file)
#         st.success("✅ File uploaded successfully!")
#         st.dataframe(df, use_container_width=True)
#     else:
#         st.info("Please upload a CSV file to view the dataset.")
import streamlit as st
import pandas as pd
import os


def render_view_dataset():
    st.header("📂 View Dataset")

    # Adjust this path to where your dataset.csv is located
    dataset_path = "dataset.csv"

    if os.path.exists(dataset_path):
        try:
            # Load only the first 1000 rows using chunks
            reader = pd.read_csv(dataset_path, chunksize=1000)
            df = next(reader)  # First chunk (first 1000 rows)
            st.success("✅ Loaded first 1000 rows successfully.")
            st.dataframe(df, use_container_width=True)

            st.caption("Showing only the first 1000 rows for performance.")

        except Exception as e:
            st.error(f"❌ Failed to read dataset: {e}")
    else:
        st.error(f"❌ File not found at: `{dataset_path}`")
