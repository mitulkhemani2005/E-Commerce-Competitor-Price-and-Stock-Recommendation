import streamlit as st
import requests

# -----------------------------
# Configuration
# -----------------------------
BASE_URL = "http://localhost:8000"

st.set_page_config(
    page_title="E-Commerce Demand Prediction",
    layout="centered"
)

st.title("📦 E-Commerce Demand & Price Prediction System")

# -----------------------------
# Backend Health Check
# -----------------------------
st.subheader("Backend Status")

if st.button("Check Backend"):
    res = requests.get(f"{BASE_URL}/")
    st.success(res.json()["Message"])


# -----------------------------
# Create Database
# -----------------------------
st.subheader("1️⃣ Create Database Schema")

if st.button("Create Database"):
    res = requests.put(f"{BASE_URL}/create-db")
    st.json(res.json())


# -----------------------------
# Fetch Product Data
# -----------------------------
st.subheader("2️⃣ Fetch Product Data (Web Scraping)")

product_url = st.text_input(
    "Enter Flipkart Product URL",
    value="https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mc6t4hn-a/p/itm7c1831ce25509"
)

if st.button("Fetch Product Data"):
    res = requests.post(
        f"{BASE_URL}/product-data-fetch",
        params={"product_url": product_url}
    )
    st.json(res.json())


# -----------------------------
# Clean Data
# -----------------------------
st.subheader("3️⃣ Clean Scraped Data")

if st.button("Run Data Cleaning"):
    res = requests.put(f"{BASE_URL}/clean-data")
    st.json(res.json())


# -----------------------------
# Rule-Based Trend Analysis
# -----------------------------
st.subheader("4️⃣ Next Day Trend (Rule-Based)")

if st.button("Analyze Trend"):
    res = requests.get(f"{BASE_URL}/next-day-trend")
    st.success(res.json()["Message"])


# -----------------------------
# Train ML Model
# -----------------------------
st.subheader("5️⃣ Train ML Model")

if st.button("Train Model"):
    res = requests.get(f"{BASE_URL}/next-model-train")
    st.json(res.json())


# -----------------------------
# ML Prediction Inputs
# -----------------------------
st.subheader("6️⃣ Predict Next Day Demand (ML Model)")

original_price = st.number_input("Original Price", min_value=0.0)
selling_price = st.number_input("Selling Price", min_value=0.0)
discount = st.number_input("Discount (%)", min_value=0.0)

overall_rating = st.number_input(
    "Overall Product Rating", min_value=0.0, max_value=5.0
)

seller_rating = st.number_input(
    "Seller Rating", min_value=0.0, max_value=5.0
)

stock = st.selectbox(
    "Availablilty",
    ["Available","Sold Out"]
)

lag_1_review = st.number_input("Lag-1 Day Review Count", min_value=0)
lag_2_review = st.number_input("Lag-2 Day Review Count", min_value=0)
rolling_3_review = st.number_input(
    "Rolling 3-Day Average Review Count", min_value=0.0
)

# -----------------------------
# Predict Button
# -----------------------------
if st.button("Predict Next Day Demand"):
    payload = {
        "original_price": original_price,
        "selling_price": selling_price,
        "discount": discount,
        "overall_rating": overall_rating,
        "stock": stock,
        "seller_rating": seller_rating,
        "lag_1_review": lag_1_review,
        "lag_2_review": lag_2_review,
        "rolling_3_review": rolling_3_review
    }

    response = requests.post(
        f"{BASE_URL}/next-day-demand",
        json=payload
    )

    if response.status_code == 200:
        st.success(response.json()["Message"])
    else:
        st.error(response.text)
