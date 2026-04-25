import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Customer Churn Prediction")
st.write("Enter customer details to predict churn:")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)

frequent_flyer = st.selectbox("Frequent Flyer", ["No", "Yes"])

annual_income = st.selectbox("Annual Income Class", 
                              ["Low Income", "Middle Income", "High Income"])

services_opted = st.number_input("Services Opted", min_value=1, max_value=8, value=3)

account_synced = st.selectbox("Account Synced To Social Media", ["No", "Yes"])

booked_hotel = st.selectbox("Booked Hotel Or Not", ["No", "Yes"])

# Encode inputs
frequent_flyer = 1 if frequent_flyer == "Yes" else 0
account_synced = 1 if account_synced == "Yes" else 0
booked_hotel = 1 if booked_hotel == "Yes" else 0

income_map = {"Low Income": 1, "Middle Income": 2, "High Income": 0}
annual_income = income_map[annual_income]

# Predict
if st.button("Predict"):
    input_data = np.array([[age, frequent_flyer, annual_income,
                            services_opted, account_synced, booked_hotel]])
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to CHURN!")
    else:
        st.success("✅ Customer is NOT likely to churn.")