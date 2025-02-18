import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(
   page_title='Multipage App',
   page_icon='❤️')
st.table(df)
st.title('Main Page')
df=pd.read_csv('Automobile.csv')
st.scatter_chart(df,x='length',y='mileage',color='company')
