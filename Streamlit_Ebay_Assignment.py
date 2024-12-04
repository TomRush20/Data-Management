import streamlit as st
import pandas as pd
import numpy as np

ebay_cleaned_df = pd.read_csv('EbayCleanedDataSample.csv')

st.header('Ebay Data by Brand')
st.divider()

unique_brands = ebay_cleaned_df['Brand'].unique()

brand = st.multiselect(label='Select a Brand', options=unique_brands)
price = st.radio(label='Select Price Range', options=['Cheap', 'Medium', 'Expensive'])

lower = 0
upper = 0
if price == 'Cheap':
    lower = 0
    upper = 500
elif price == 'Medium':
    lower = 500
    upper = 1000
else:
    lower = 1000
    upper = 3000

filtered = ebay_cleaned_df[(ebay_cleaned_df['Brand'].isin(brand)) & ((ebay_cleaned_df['Price'] >= lower) & 
                           (ebay_cleaned_df['Price'] < upper))]
st.dataframe(filtered, use_container_width=True)
