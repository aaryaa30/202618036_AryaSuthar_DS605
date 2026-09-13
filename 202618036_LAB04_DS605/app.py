import streamlit as st
import pandas as pd
import numpy as np
import joblib


# -------------------------------------------------
# Page configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Airbnb Price Prediction",
    page_icon="🏠",
    layout="centered"
)


# -------------------------------------------------
# Load trained model
# -------------------------------------------------

@st.cache_resource
def load_model():
    return joblib.load("airbnb_price_pipeline.pkl")


model = load_model()


# -------------------------------------------------
# Application title
# -------------------------------------------------

st.title("🏠 Airbnb Price Prediction")
st.write(
    "Enter the details of an Airbnb listing to estimate "
    "its nightly price in New York City."
)


# -------------------------------------------------
# User inputs
# -------------------------------------------------

neighbourhood_group = st.selectbox(
    "Neighbourhood Group",
    [
        "Manhattan",
        "Brooklyn",
        "Queens",
        "Bronx",
        "Staten Island"
    ]
)

neighbourhood = st.text_input(
    "Neighbourhood",
    value="Harlem"
)

latitude = st.number_input(
    "Latitude",
    value=40.7128,
    format="%.4f"
)

longitude = st.number_input(
    "Longitude",
    value=-74.0060,
    format="%.4f"
)

room_type = st.selectbox(
    "Room Type",
    [
        "Entire home/apt",
        "Private room",
        "Shared room"
    ]
)

minimum_nights = st.number_input(
    "Minimum Nights",
    min_value=1,
    max_value=365,
    value=3
)

number_of_reviews = st.number_input(
    "Number of Reviews",
    min_value=0,
    value=10
)

reviews_per_month = st.number_input(
    "Reviews per Month",
    min_value=0.0,
    value=1.0,
    format="%.2f"
)

calculated_host_listings_count = st.number_input(
    "Host Listing Count",
    min_value=1,
    value=1
)

availability_365 = st.number_input(
    "Availability in a Year",
    min_value=0,
    max_value=365,
    value=200
)


# -------------------------------------------------
# Prediction
# -------------------------------------------------

if st.button("Predict Airbnb Price"):

    input_data = pd.DataFrame({
        "neighbourhood_group": [neighbourhood_group],
        "neighbourhood": [neighbourhood],
        "latitude": [latitude],
        "longitude": [longitude],
        "room_type": [room_type],
        "minimum_nights": [minimum_nights],
        "number_of_reviews": [number_of_reviews],
        "reviews_per_month": [reviews_per_month],
        "calculated_host_listings_count": [
            calculated_host_listings_count
        ],
        "availability_365": [availability_365]
    })

    predicted_log_price = model.predict(input_data)

    predicted_price = np.expm1(predicted_log_price[0])

    st.success(
        f"Estimated nightly price: ${predicted_price:,.2f}"
    )

    st.info(
        "This is an estimated price based on patterns learned "
        "from the Airbnb dataset."
    )