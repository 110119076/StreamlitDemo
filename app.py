import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title("Streamlit App Demo")

# Display simple text
st.write("This is Benky")

df = pd.DataFrame({
    'col1': [1,2,3,4],
    'col2': [10,20,30,40]
})

# Displaying a dataframe
st.write(df)

# Line chart
chart_data = pd.DataFrame(np.random.randn(15,3), columns=['col1','col2','col3'])
st.line_chart(chart_data)
