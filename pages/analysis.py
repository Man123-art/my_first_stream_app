import streamlit as st
import pandas as pd
st.set_page_config(
   page_title='Multipage App',
   page_icon='❤️')
st.title('Main Page')
df=pd.read_csv('Automobile.csv')
st.table(df)
st.scatter_chart(df,x='length',y='mileage',color='company')
