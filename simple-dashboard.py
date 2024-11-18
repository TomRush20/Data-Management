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