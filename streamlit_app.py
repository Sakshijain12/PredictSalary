import streamlit as st
from predict import predict_page
from explore import explore_page


page = st.sidebar.selectbox("Explore Or Predict", ("Explore", "Predict"))

if page == "Predict":
    predict_page()
else:
    explore_page()