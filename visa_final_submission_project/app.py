
# Streamlit App
import streamlit as st
import pickle

st.title("Visa Processing Time Estimator")

model = pickle.load(open("visa_model.pkl","rb"))

visa = st.number_input("Visa Class")
status = st.number_input("Case Status")
work = st.number_input("Worksite")
year = st.number_input("Year")

if st.button("Predict"):
    pred = model.predict([[visa,status,work,year]])
    st.success(f"Estimated Days: {int(pred[0])}")
