import streamlit as st
import pickle
import numpy as np

# Load the trained pipeline
with open(r"house_price_pipeline.pkl", "rb") as f:
    pipeline = pickle.load(f)

st.title("🏠 House Price Prediction App")

# Input fields
area = st.number_input("Area (sq ft)", min_value=100, max_value=10000, value=1000)
bedroom = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=2)
bathroom = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
additional_room = st.selectbox("Additional Room", ["Yes", "No"])
balcony = st.selectbox("Balcony Count", ["0", "1", "2", "3", "3+"])
floor_num = st.number_input("Floor Number", min_value=0, max_value=50, value=1)
facing = st.selectbox("Facing Direction", ["East", "West", "North", "South", "North-East", "South-East", "North-West", "South-West"])
age_possession = st.selectbox("Age/Possession", ["New", "Mid", "Old", "Very Old", "Under Construction"])

# Convert 'Yes'/'No' to binary
additional_room_binary = 1 if additional_room == "Yes" else 0

# Predict button
if st.button("Predict Price"):
    input_data = np.array([[area, bedroom, bathroom, additional_room_binary, balcony, floor_num, facing, age_possession]])
    predicted_price = pipeline.predict(input_data)[0]
    st.success(f"Estimated House Price: ₹{predicted_price:,.2f} crore")