import streamlit as st
from components import sidebar


def main():
    st.set_page_config(layout="wide")

    # Render sidebar
    sidebar.render_sidebar()


if __name__ == "__main__":
    main()
