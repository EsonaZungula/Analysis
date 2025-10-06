import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title(" Crime Hotspot & Drone Simulation Dashboard")

uploaded_file = st.file_uploader(" Upload your dataset (CSV)", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.success(" Data uploaded successfully!")
    st.write(data.head())

    st.subheader(" Category Distribution")
    if 'Crime Category' in data.columns:
        fig, ax = plt.subplots()
        sns.countplot(data=data, x='Crime Category', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.warning("No 'Crime Category' column found in your dataset.")
else:
    st.info("Please upload a CSV file to start.")
