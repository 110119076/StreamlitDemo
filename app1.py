import streamlit as st
import pandas as pd

st.title("Streamlit Demo 2")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello {name}")

age = st.slider("Select your age: ", 0, 150, 25)

st.write(f"Your Age is {age}")

options = ["Python", "Java", "C++", "Go", "JavaScript"]
choice = st.selectbox("Choose your favorite programming language:", options)

st.write(f"You selected {choice}")


data = {
    "Name": ["Ippo", "Miyata", "Aoki", "Takamura"],
    "Age": [14,15,21,24],
    "City": ["Tokyo", "Chicago", "Houston", "Misissipi"]
}

df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

