import streamlit as st
import pandas as pd



st.title("Engineering Exams")



df=pd.read_csv("after12th.csv")

st.write(df)





