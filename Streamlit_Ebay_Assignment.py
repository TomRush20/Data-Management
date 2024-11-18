import streamlit as st
import pandas as pd
import numpy as np

ebay_cleaned_df = pd.read_csv(r"C:\Users\trush\OneDrive\Documents\WFU Grad School Info\BAN 6020 Data Management\Data\CleanRewardsData.csv")

st.header('Ebay Data')
st.divider()

st.subheader('Data Table')
st.dataframe(ebay_cleaned_df, use_container_width=True)

state_totals = ebay_cleaned_df.groupby('State Name')['Total Points Earned'].sum()

st.subheader('Total Points Earned Per State')
st.bar_chart(state_totals, horizontal=True)