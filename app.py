import streamlit as st
import pandas as pd

uploaded_files = st.file_uploader("Upload your files (csv or excel)", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    st.write("Files uploaded successfully!")

    for uploaded_file in uploaded_files:
        file_ext = uploaded_file.name.split('.')[-1]  # File extension le rahe hain
        if file_ext == "csv":
            df = pd.read_csv(uploaded_file)
            st.write(df)
        elif file_ext in ["xls", "xlsx"]:
            df = pd.read_excel(uploaded_file)
            st.write(df)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            

        

