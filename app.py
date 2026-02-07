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

age = st.number_input("Age", min_value=1, max_value=100, value=30)
sex = st.number_input("Sex (0/1)", min_value=0, max_value=1, value=0)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1)
bp  = st.number_input("BP", min_value=50.0, max_value=150.0, value=80.0, step=0.5)
s1  = st.number_input("S1", value=0.0)
s2  = st.number_input("S2", value=0.0)
s3  = st.number_input("S3", value=0.0)
s4  = st.number_input("S4", value=0.0)
s5  = st.number_input("S5", value=0.0)
s6  = st.number_input("S6", value=0.0)

if st.button("Predict"):
    data = np.array([[age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]])
    new_data = scaler.transform(data)
    output = regmodel.predict(new_data)
    st.success(f"Predicted diabetes progression: {output[0].item():.2f}")

st.markdown("---")
st.write("**Note:** This is a predictive model and should not replace professional medical advice.")
st.write("Created by: [Jonnagiri Vamsi Krishna JVK] | [LinkedIn : https://www.linkedin.com/in/vamsi-krishna-4210a1325/ ,GitHub : https://github.com/vamsi-krishna108]")
