import streamlit as st
import pickle
import numpy as np

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="wide"
)

# ---------------------- LOAD MODEL -----------------------
model = pickle.load(open("diabetes_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ---------------------- CUSTOM CSS -----------------------
st.markdown("""
<style>

.main{
    background-color:#f8f9fa;
}

.title{
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#0E76A8;
}

.subtitle{
    text-align:center;
    color:gray;
    font-size:18px;
    margin-bottom:30px;
}

.stButton>button{
    width:100%;
    height:55px;
    background-color:#0E76A8;
    color:white;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background-color:#055a8c;
    color:white;
}

.result-success{
    padding:20px;
    border-radius:10px;
    background:#d4edda;
    color:#155724;
    font-size:22px;
    font-weight:bold;
    text-align:center;
}

.result-danger{
    padding:20px;
    border-radius:10px;
    background:#f8d7da;
    color:#721c24;
    font-size:22px;
    font-weight:bold;
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------- SIDEBAR ----------------------

st.sidebar.title("📌 Project Information")

st.sidebar.success("Machine Learning Project")

st.sidebar.write("### Algorithm")
st.sidebar.info("K-Nearest Neighbors (KNN)")

st.sidebar.write("### Best K Value")
st.sidebar.success("8")

st.sidebar.write("### Accuracy")
st.sidebar.success("76.62%")

st.sidebar.write("### Dataset")
st.sidebar.info("Pima Indians Diabetes Dataset")

st.sidebar.write("---")

st.sidebar.write("Developed By")
st.sidebar.write("**Shruti Yadav**")

# ---------------------- TITLE ----------------------

st.markdown('<p class="title">🩺 Diabetes Prediction System</p>', unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">Predict whether a patient is likely to have Diabetes using Machine Learning.</p>',
    unsafe_allow_html=True
)

# ---------------------- INPUTS ----------------------

col1, col2 = st.columns(2)

with col1:

    pregnancies = st.number_input("Pregnancies",0,20,1)

    glucose = st.number_input("Glucose",0.0,300.0,120.0)

    blood_pressure = st.number_input("Blood Pressure",0.0,200.0,70.0)

    skin_thickness = st.number_input("Skin Thickness",0.0,100.0,20.0)

with col2:

    insulin = st.number_input("Insulin",0.0,900.0,80.0)

    bmi = st.number_input("BMI",0.0,70.0,25.0)

    dpf = st.number_input("Diabetes Pedigree Function",0.0,3.0,0.5)

    age = st.number_input("Age",1,120,30)

st.write("")

# ---------------------- BUTTON ----------------------

if st.button("🔍 Predict Diabetes"):

    input_data = np.array([[

        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        dpf,
        age

    ]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    st.write("")

    st.subheader("Prediction Result")

    if prediction[0] == 1:

        st.markdown(
            '<div class="result-danger">⚠️ High Risk of Diabetes</div>',
            unsafe_allow_html=True
        )

        st.warning("Please consult a healthcare professional for proper medical diagnosis.")

    else:

        st.markdown(
            '<div class="result-success">✅ Low Risk of Diabetes</div>',
            unsafe_allow_html=True
        )

        st.success("The patient is less likely to have Diabetes.")

# ---------------------- FOOTER ----------------------

st.markdown("---")

st.markdown(
"""
<div class="footer">

Developed using ❤️ with <b>Streamlit</b> | <b>Scikit-Learn</b>

<br>

KNN Diabetes Prediction Project

</div>
""",
unsafe_allow_html=True)