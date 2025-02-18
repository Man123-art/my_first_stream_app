import streamlit as st
import pandas as pd
st.set_page_config(
   page_title='Multipage App')
 
st.title('Mathematician')
st.header('Aryabhat',divider=True)
col1,col2 = st.columns(2)
with col1:
    st.image("images.jpg")
with col2:
    st.text('Aryabhata, a famed Indian mathematician and astronomer of the 5th century AD, significantly contributed to the evolution of mathematical concepts, including zero')

df=pd.read_csv('Automobile.csv')
st.dataframe(data=df)

