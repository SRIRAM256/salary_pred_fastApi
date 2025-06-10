import requests
import streamlit as st
from models.user_input_validation import UserInput, job_level


API_URL = "http://127.0.0.1:8000/predict"

st.title("User Input Form")

age = st.number_input("Age", min_value=1, max_value=119, value=25)
gender = st.radio("Gender", options=["Male", "Female"])
education = st.selectbox("Education Level", ["Bachelor's", "Master's", 'PhD', "Bachelor's Degree", "Master's Degree", 'High School', 'phD'])
job = st.selectbox("Job Title", job_level)
experience = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, step=0.1)

if st.button("Submit"):
    try:
        user_input = UserInput(
            Age=age,
            Gender=gender,
            Education_Level=education,
            Job_Title=job,
            Years_of_Experience=experience
        )

        
        response=requests.post(API_URL,json=dict(user_input))
        
        if(response.status_code==200):
            result=response.json()
            st.markdown(result['prediction'])
        else:
            st.error(response.text)
    except Exception as e:
        st.error(f"❌ Validation error: {e}")