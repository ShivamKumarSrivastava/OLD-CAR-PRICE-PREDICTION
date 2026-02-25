import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Used Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)
# Load model
model = joblib.load("Model/model.pkl")

# Mappings

model_mapping = joblib.load("Notebook/model_mapping.pkl")
make_model_dict = joblib.load("Notebook/make_model_dict.pkl")

fuel_mapping = {
    'petrol': 1,
    'diesel': 2,
    'petrol & cng': 3,
    'petrol & lpg': 4
}

body_mapping = {
    'hatchback': 1,
    'sedan': 2,
    'suv': 3,
    'luxury sedan': 4,
    'luxury suv': 5
}

transmission_mapping = {
    'manual': 1,
    'automatic': 2
}

state_mapping = {
    "delhi": 1,
    "uttar pradesh": 2,
    "haryana": 3,
    "maharashtra": 4,
    "karnataka": 5,
    "gujarat": 6,
    "jharkhand": 7,
    "punjab": 8,
    "telangana": 9,
    "andhra pradesh": 10,
    "west bengal": 11,
    "tamil nadu": 12,
    "uttarakhand": 13
}

make_mapping = {
    "maruti": 1,
    "hyundai": 2,
    "renault": 3,
    "honda": 4,
    "ford": 5,
    "nissan": 6,
    "toyota": 7,
    "tata": 8,
    "datsun": 9,
    "mahindra": 10,
    "volkswagen": 11,
    "audi": 12,
    "mercedes benz": 13,
    "chevrolet": 14,
    "bmw": 15,
    "skoda": 16,
    "volvo": 17,
    "fiat": 18,
    "isuzu": 19,
    "ssangyong": 20,
    "jeep": 21
}

car_rating_mapping = {
    'great' : 1,
    'good' : 2,
    'fair' : 3,
    'overpriced' : 4
}

warranty_mapping = {
    "Available": 1,
    "Not Available": 2
}

st.title("🚗 Used Car Sale Price Prediction")

# Inputs
make = st.selectbox("Car Company", sorted(make_model_dict.keys()))

model_name = st.selectbox(
    "Car Model",
    make_model_dict[make]
)

fuel_type = st.selectbox("Fuel Type", sorted(fuel_mapping.keys()))
body_type = st.selectbox("Body Type", sorted(body_mapping.keys()))

yr_mfr = st.number_input("Manufacturing Year", min_value=1990, max_value=2026)
kms_run = st.number_input("Kilometers Driven", min_value=0)

transmission = st.selectbox("Transmission", sorted(transmission_mapping.keys()))
registered_state = st.selectbox("Registered State", sorted(state_mapping.keys()))

total_owners = st.selectbox("Total Owners", [0, 1, 2, 3, 4, 5])

car_rating = st.selectbox("Car Rating", list(car_rating_mapping.keys()))

warranty_avail = st.selectbox("Warranty Available", sorted(warranty_mapping.keys()))

# Prediction
if st.button("Predict Sale Price"):

    user_input = {
        "yr_mfr": yr_mfr,
        "fuel_type": fuel_mapping.get(fuel_type, 0),
        "kms_run": kms_run,
        "body_type": body_mapping.get(body_type, 0),
        "transmission": transmission_mapping.get(transmission, 0),
        "registered_state": state_mapping.get(registered_state, 0),
        "make": make_mapping.get(make, 0),
        "model": model_mapping.get(model_name, 0),
        "total_owners": total_owners,
        "car_rating": car_rating_mapping.get(car_rating, 0),
        "warranty_avail": warranty_mapping.get(warranty_avail, 0)
    }

    input_df = pd.DataFrame([user_input])

    prediction = model.predict(input_df)

    st.success(f"Estimated Sale Price: ₹ {round(prediction[0], 2)}")

