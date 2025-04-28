import streamlit as st
from predict import predict_churn

st.title("🔮 Customer Churn Prediction App")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Income", min_value=1000, max_value=100000, value=50000)
activity_score = st.slider("Activity Score", 0, 100, 50)

if st.button("Predict Churn"):
    result = predict_churn(age, income, activity_score)
    if result == 1:
        st.error("⚠️ Customer is likely to CHURN!")
    else:
        st.success("✅ Customer is likely to STAY!")

