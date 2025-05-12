import streamlit as st
import pandas as pd

st.title("BMI Calculator")

height = st.slider("Enter your height (in cms):" ,100,250,175)
weight = st.slider("Enert your weight (in kg)" ,40, 200,70)

bmi = weight / ((height / 100)  ** 2)

st.write(f"Your BMI is  {bmi:.2f}")

st.write ("### BMI Catogories ###")
st.write ("- underweight: BMI less than 18.5")
st.write ("- Normal Weight: BMI between 18.5 to 24.9")
st.write ("- Over Weight: BMI between 25 to 29.9")
st.write ("- Obasity: BMI 30 or greater")