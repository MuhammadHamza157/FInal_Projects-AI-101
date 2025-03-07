import streamlit as st
import pandas as pd
st.title("BMI CALCULATOR")

height = st.slider("Enter your height in inch", 30,100,50)
weight = st.slider("Enter your weight in kg", 40, 130,65)


height_in_meter = height / 37.39

bmi = weight /height_in_meter **2

st.write(f"Your BMI is equal to: {bmi:.2f}")

if bmi<=18.5:
     st.write(f"UNDERWIEGHT")
     st.image(r"C:\Users\PAK COMPUTER\Desktop\final_projects\underweight.PNG")
elif 24.9>=bmi>18.5:
       st.write(f"NORMAL WIEGHT")
       st.image(r"C:\Users\PAK COMPUTER\Desktop\final_projects\normal.PNG")
elif   29.9>= bmi>24.9:
         st.write(f"Over WIEGHT")
         st.image(r"C:\Users\PAK COMPUTER\Desktop\final_projects\overweight.PNG")
elif  bmi>29.9:
         st.write(f"OBESE")  
         st.image(r"C:\Users\PAK COMPUTER\Desktop\final_projects\obese.PNG")

