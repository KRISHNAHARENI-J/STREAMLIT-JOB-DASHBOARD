import streamlit as st
import pandas as pd

st.title("Excel Data Upload")

# Upload Excel file
uploaded_file = st.file_uploader(
    "Upload your Excel file",
    type=["xlsx", "xls"]
)

if uploaded_file is not None:

    # Read Excel file
    df = pd.read_excel(uploaded_file)

    st.success("Excel file uploaded successfully!")

    # Show data
    st.subheader("Uploaded Data")
    st.dataframe(df)

    # Show number of rows and columns
    st.write("Number of rows:", df.shape[0])
    st.write("Number of columns:", df.shape[1])