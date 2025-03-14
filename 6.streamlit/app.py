import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title('My first Streamlit application')

st.write('This is a simple application')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

## Display the dataframe
st.write("The dataframe")
st.write(df)


## Display a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)