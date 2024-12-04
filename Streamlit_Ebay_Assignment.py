import streamlit as st
import pandas as pd
import numpy as np

ebay_cleaned_df = pd.read_csv('EbayCleanedDataSample.csv')

st.header('Ebay Data by Brand')
st.divider()

unique_brands = ebay_cleaned_df['Brand'].unique()
unique_os = ebay_cleaned_df['OS'].unique()

brand = st.selectbox(label='Select a Brand', options=unique_brands)
OS = st.radio(label='Select color', options=unique_os)

if OS:
    filtered = ebay_cleaned_df[(ebay_cleaned_df['Brand'] == brand) & (ebay_cleaned_df['OS'] == OS)]
    st.dataframe(filtered, use_container_width=True)
else:
    st.write('Choose an OS')