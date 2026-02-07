import pickle
import numpy as np
import streamlit as st

# Load model and scaler
regmodel = pickle.load(open('regmodel.pkl','rb'))
scaler = pickle.load(open('scaling.pkl','rb'))

st.title("Diabetes Predictions")
st.title("🏥 Diabetes Prediction System")
st.write("""
This ML model predicts the likelihood of diabetes based on medical parameters.
Built using Linear Regression algorithm with 77% accuracy.
""")

st.markdown("---")  # Divider line

age = st.number_input("Age")
sex = st.number_input("Sex ")
bmi = st.number_input("BMI")
bp  = st.number_input("BP")
s1  = st.number_input("S1")
s2  = st.number_input("S2")
s3  = st.number_input("S3")
s4  = st.number_input("S4")
s5  = st.number_input("S5")
s6  = st.number_input("S6")

if st.button("Predict"):
    data = np.array([[age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]])
    new_data = scaler.transform(data)
    output = regmodel.predict(new_data)
    st.success(f"Predicted diabetes progression: {output[0].item():.2f}")

st.markdown("---")
st.write("**Note:** This is a predictive model and should not replace professional medical advice.")
st.write("Created by: [Jonnagiri Vamsi Krishna JVK] | [LinkedIn : https://www.linkedin.com/in/vamsi-krishna-4210a1325/ ,GitHub : https://github.com/vamsi-krishna108]")
