# =========================================
# 🏭 STREAMLIT APP FOR SMART MODEL
# =========================================

import streamlit as st
import pickle
import numpy as np

# =========================================
# 📦 Load Model
# =========================================
model = pickle.load(open('model.pkl', 'rb'))

# =========================================
# 🎨 UI Design
# =========================================
st.title("🏭 Smart Manufacturing Prediction System")
st.write("Enter sensor values to predict machine status")

# =========================================
# 🧾 User Inputs (Example Inputs)
# ⚠️ Change based on your dataset columns
# =========================================

temperature = st.number_input("Temperature")
humidity = st.number_input("Humidity")
vibration = st.number_input("Vibration")
pressure = st.number_input("Pressure")

# Convert input into array
input_data = np.array([[temperature, humidity, vibration, pressure]])

# =========================================
# 🔮 Prediction
# =========================================
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Prediction: {prediction[0]}")
