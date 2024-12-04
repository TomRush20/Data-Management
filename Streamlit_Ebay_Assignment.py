import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

ebay_cleaned_df = pd.read_csv('EbayCleanedDataSample.csv')

def Brand_Exploration():
    st.header('Laptop Data by Brand')
    st.divider()

    unique_brands = ['All'] + ebay_cleaned_df['Brand'].unique().tolist()

    brand = st.multiselect(label='Select a Brand', options=unique_brands, default='All')
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


    if 'All' not in brand:
        filtered = ebay_cleaned_df[(ebay_cleaned_df['Brand'].isin(brand)) & ((ebay_cleaned_df['Price'] >= lower) & 
                                    (ebay_cleaned_df['Price'] < upper))]
    else:
        filtered = ebay_cleaned_df[(ebay_cleaned_df['Price'] >= lower) & (ebay_cleaned_df['Price'] < upper)]


    st.dataframe(filtered, use_container_width=True)

def Screen_Size_vs_Price():
    st.header('Screen Size vs. Price')

    data = ebay_cleaned_df

    data['Screen Size'] = data['Screen Size'].str.replace('in', '')
    data['Screen Size'] = data['Screen Size'].astype(float)

    st.scatter_chart(data, x='Screen Size', y='Price', use_container_width=True)

    st.subheader('Analysis')

    st.write("""As we can see there is not much of a relationship between screen size and price. 
    Price is a maximum where the screen size is 14 in. However, there is a wide range of cheap and expensive laptops that are 14 in. 
    This may be a popular screen size for customers.""")

def Distribution_Of_Laptop_Prices():
    st.header('Distribution of Laptop Prices')

    data = ebay_cleaned_df

    price_histogram = px.histogram(data, x='Price')

    st.plotly_chart(price_histogram, use_container_width=True)

    st.subheader('Analysis')
    st.write("""As we can see the distribution of the price is skewed to the left. We are primarily selling cheap laptops.
    We should target advertisements towards people who are looking for cheap hardware. We should also target advertising
    towards businesses that need more hardware, and do not need much processing power to run their programs.""")

def Comparing_Models():
    st.header('Comparing Models')

    data = ebay_cleaned_df

    input = st.text_input(label='Type in a Brand: (Enter to Continue)')

    if input in data['Brand'].unique():
        second_input = st.text_input(label='Type in a second Brand: (Enter to Continue)')
        if second_input in data['Brand'].unique():

            brands_to_compare = [input, second_input]
            compared_brands = data[data['Brand'].isin(brands_to_compare)]
            compared_brands = compared_brands[['Brand', 'Model', 'Price']]

            compared_brands = compared_brands.groupby(['Brand', 'Model']).mean().reset_index()

            bar_chart = px.bar(compared_brands, x='Price', y='Model', color='Brand')
            st.plotly_chart(bar_chart, use_container_width=True)

        else:
            st.write('Type in a valid brand.')
    else:
        st.write('Type in a valid brand.')
    
    
    

pages = {
    'Ebay Laptop Data Analysis': [st.Page(Brand_Exploration), st.Page(Screen_Size_vs_Price), 
    st.Page(Distribution_Of_Laptop_Prices), st.Page(Comparing_Models)]
}
pg = st.navigation(pages)
pg.run()
