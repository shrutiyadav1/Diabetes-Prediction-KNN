# Diabetes-Prediction-KNN
A Machine Learning web application for diabetes prediction using K-Nearest Neighbors (KNN) and Streamlit.
# 🩺 Diabetes Prediction System

This project is a Machine Learning application that predicts whether a person is likely to have diabetes based on their medical information. I built this project to strengthen my understanding of the K-Nearest Neighbors (KNN) algorithm and to gain hands-on experience in building and deploying an end-to-end Machine Learning project.

The application is developed using **Python**, **Scikit-learn**, and **Streamlit**.

---

## 📖 About the Project

While learning Machine Learning, I wanted to build a project that covered the complete workflow instead of only training a model.

In this project, I worked on:

- Understanding the dataset
- Cleaning and preprocessing the data
- Handling missing values
- Applying feature scaling
- Training a KNN classifier
- Finding the best value of K
- Evaluating the model
- Deploying the trained model using Streamlit

This project helped me understand how Machine Learning models are used in real-world applications.

---

## 📂 Dataset

The project uses the **Pima Indians Diabetes Dataset**, which contains medical information of patients.

### Features

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### Target

**Outcome**

- 0 → Non-Diabetic
- 1 → Diabetic

---

## ⚙️ Project Workflow

1. Loaded the dataset using Pandas.
2. Explored the data and checked for missing values.
3. Replaced invalid values and performed preprocessing.
4. Split the dataset into training and testing sets.
5. Applied StandardScaler for feature scaling.
6. Trained the KNN model.
7. Tested multiple K values to select the best one.
8. Evaluated the model using Accuracy, Confusion Matrix, and Classification Report.
9. Saved the trained model using Pickle.
10. Built an interactive Streamlit web application.

---

## 🤖 Model Information

**Algorithm Used**

K-Nearest Neighbors (KNN)

**Best K Value**

8

**Model Accuracy**

**76.62%**

---

## 💻 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Pickle

---

## 📸 Application Preview

(Add your Streamlit screenshot here)

```
screenshot.png
```

---

## 🚀 How to Run

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Diabetes-Prediction-KNN
│
├── app.py
├── diabetes_model.pkl
├── scaler.pkl
├── Diabetes_prediction.csv
├── Diabetes_Prediction.ipynb
├── requirements.txt
└── README.md
```

---

## 🌱 What I Learned

This project helped me improve my understanding of:

- Data preprocessing
- Feature scaling
- K-Nearest Neighbors (KNN)
- Model evaluation
- Streamlit deployment
- Saving and loading Machine Learning models

Building this project also gave me confidence in creating complete Machine Learning applications from scratch.

---

## 👩‍💻 About Me

I'm **Shruti Yadav**, a B.Tech CSE (AI) student who is currently learning Machine Learning by building practical projects.

My goal is to improve my skills through hands-on development and gradually build a strong Machine Learning portfolio.

If you have any suggestions to improve this project, I'd be happy to learn from your feedback.

⭐ Thank you for visiting my repository!
