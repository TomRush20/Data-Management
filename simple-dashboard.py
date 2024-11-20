import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout='wide')

#Create streamlit app and display some text
st.header('Welcome to Streamlit!')
st.divider()
st.write('Streamlit makes data visualizations interactive and easy!')

#Dataframes
df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

st.subheader('Sample Pandas DataFrame')
st.dataframe(df, use_container_width=True)

#Charts
st.subheader('Line Chart')
st.line_chart(df)

st.subheader('Bar Chart')
st.bar_chart(df)

st.subheader('Area Chart')
st.area_chart(df)

st.subheader('Scatter Chart')
st.scatter_chart(df)

#Column Separation
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label='Current Temperature', value='32 F', delta='5 F')
with col2:
    st.metric(label='24hr Snowfall', value='5 in', delta='2 in')
with col3:
    st.metric(label='Humidity', value='30%', delta='5%')

#Containers
simple_container = st.container(border=True)
simple_container.write('This text is inside of the container')

st.write('This is outside the continer')

#Tabs
st.subheader('Tabbed Container')

tab1, tab2, tab3 = st.tabs(['Cat', 'Dog', 'Owl'])

with tab1:
    st.header('This is a cat')
    st.image('https://static.streamlit.io/examples/cat.jpg', width=200)
with tab2:
    st.header('This is a dog')
    st.image('https://static.streamlit.io/examples/dog.jpg', width=200)
with tab3:
    st.header('This is a owl')
    st.image('https://static.streamlit.io/examples/owl.jpg', width=200)

clicked = st.button('Click Me', type='primary')
if st.button('Click Me'):
    st.image('slap-face.gif')

sales_df = pd.read_csv(r"C:\Users\trush\OneDrive\Documents\WFU Grad School Info\BAN 6020 Data Management\Data\walmart_sales_data.csv")
st.subheader('Sales Records')
st.dataframe(sales_df, use_container_width=True)

#Single Select
st.subheader('Sales Records Filtered by Holiday')
holiday_options = sales_df['Holiday_Flag'].unique()
holiday_selection = st.selectbox('Holiday Week? (1=yes, 0=no)', options=holiday_options)
filtered_df_selectbox = sales_df[sales_df['Holiday_Flag'] == holiday_selection]
st.dataframe(filtered_df_selectbox, use_container_width=True)

#Multi-select
st.subheader('Sales Records Filtered by Store Number')
store_options = sales_df['Store'].unique()
store_selection = st.multiselect('Choose a Store: ', options=store_options, default=1)
filtered_by_store = sales_df[sales_df['Store'].isin(store_selection)]
st.dataframe(filtered_by_store, use_container_width=True)

sales_df['Date'] = pd.to_datetime(sales_df['Date'], infer_datetime_format=True)

st.subheader('Sales Records Filtered by Date Range')

min_date = sales_df['Date'].min()
max_date = sales_df['Date'].max()
start_date = min_date
end_date = max_date

start_date = st.date_input('Select Start Date: ', min_date, min_value=min_date, max_value=max_date)
end_date = st.date_input('Select End Date: ', max_date, min_value=min_date, max_value=max_date)

start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

if start_date and end_date and start_date < end_date:
    filtered_by_date = sales_df[(sales_df['Date'] >= start_date) & (sales_df['Date'] <= end_date)]
    filtered_by_date['Date'] = filtered_by_date['Date'].sort_values()
    st.dataframe(filtered_by_date, use_container_width=True)
else:
    st.error('Invalid Date Range Selected')


import plotly.express as px
df = px.data.gapminder()
scatter = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
st.plotly_chart(scatter)

iris_df = px.data.iris()
st.dataframe(iris_df)
st.subheader('Iris Dataset Basic Scatterplot')
basic_scatter_fig = px.scatter(iris_df, x='sepal_width', y='sepal_length', animation_frame='species', color='species')
st.plotly_chart(basic_scatter_fig)