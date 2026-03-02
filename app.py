import streamlit as st
import pickle
import numpy as np

# Load Model
model = pickle.load(open("your_model.pkl", "rb"))

st.set_page_config(page_title="Kraljic Matrix Predictor", layout="centered")

st.title("📦 Kraljic Matrix Category Predictor")
st.write("Enter procurement details to predict the Kraljic Category")

# User Inputs
lead_time = st.number_input("Lead Time (Days)", min_value=0)
order_volume = st.number_input("Order Volume (Units)", min_value=0)
cost_per_unit = st.number_input("Cost per Unit")
supply_risk = st.slider("Supply Risk Score", 0, 10)
profit_impact = st.slider("Profit Impact Score", 0, 10)
environmental_impact = st.slider("Environmental Impact", 0, 10)
single_source_risk = st.slider("Single Source Risk", 0, 10)

# Predict Button
if st.button("Predict Category"):
    input_data = np.array([[lead_time,
                            order_volume,
                            cost_per_unit,
                            supply_risk,
                            profit_impact,
                            environmental_impact,
                            single_source_risk]])
    
    prediction = model.predict(input_data)
    
    st.success(f"Predicted Kraljic Category: {prediction[0]}")
