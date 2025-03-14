import streamlit as st
import pandas as pd 
st.title("Stremlit text input")

name = st.text_input("Enter your name")


age = st.slider("Whats your age  ?" , 0,100,25)
st.write(f"Your age is {age}.")

options = ["Python", "Java", "C++" , "JavaScript"]
choice = st.selectbox("Which programming language do you use ?", options)
st.write(f"You selected {choice}")

if name:
    st.write(f"Hello {name}")

df = pd.DataFrame({
    "Name" : ["John","Jane" ,"Jake","Jill"],
    "Age" : [20,30,40,50],
    "City" : ["New York","Bihar","Los Angeles","Chicago"]
})

st.write(df)

uploaded_file = st.file_uploader("Choose a CSv file" , type = "csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)