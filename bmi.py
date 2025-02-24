import streamlit as st
import pandas as pd
import plotly.express as px

def calculate_bmi(weight, height_ft, height_inch):
    height_cm = (height_ft * 30.48) + (height_inch * 2.54)  # Convert feet and inches to cm
    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight", "#3498db"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "#2ecc71"
    elif 25 <= bmi < 29.9:
        return "Overweight", "#f1c40f"
    else:
        return "Obese", "#e74c3c"
    
st.set_page_config(page_title="BMI Calculator", page_icon="⚖", layout="centered")
st.title("🏋️ BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) and check your health status.")

weight = st.slider("Select your weight (kg):", 30, 150, 70)
height_ft = st.slider("Select your height (feet):", 4, 7, 5)
height_inch = st.slider("Select your height (inches):", 0, 11, 6)

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height_ft, height_inch)
    category, color = classify_bmi(bmi)
    
    st.markdown(f"<h2 style='color:{color};'>Your BMI: {bmi} ({category})</h2>", unsafe_allow_html=True)
    
    bmi_categories = ["Underweight", "Normal weight", "Overweight", "Obese"]
    bmi_values = [18.5, 24.9, 29.9, 35]
    df = pd.DataFrame({"Category": bmi_categories, "Weight (kg)": bmi_values})
    fig = px.bar(df, x="Category", y="Weight (kg)", color="Category", text_auto=True,
                 color_discrete_map={
                     "Underweight": "#3498db",
                     "Normal weight": "#2ecc71",
                     "Overweight": "#f1c40f",
                     "Obese": "#e74c3c"
                 })
    st.plotly_chart(fig)
