import streamlit as st
import pandas as pd
import numpy as np


df_data= pd.read_csv('img.txt',skiprows=1,skipfooter=1,engine='python',sep=';')


st.title('BPI - app')
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    string_data = stringio.read()

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file,skiprows=1,skipfooter=1,engine='python',sep=';')
    # st.write(dataframe)
    st.dataframe(dataframe)

# btn = st.button("Click")
# if btn:
#     st.dataframe(df_data)
#     st.download_button(
#         label="Download data as CSV",
#         data=df_data.to_csv().encode('utf-8'),
#         file_name='my_file.csv',
#         mime='text/csv',
#     )    
