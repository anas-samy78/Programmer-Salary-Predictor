![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-XGBoost-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

# 💻 Programmer Salary Predictor

🚀 **Live Demo:** https://programmer-salary-predictor.streamlit.app/

## 📌 Project Overview

The **Programmer Salary Predictor** is a Machine Learning project designed to estimate a programmer's salary based on professional, educational, and workplace-related factors.

The project combines data preprocessing, feature engineering, model training, and deployment into an interactive web application that allows users to predict salaries instantly.

---

## 🎯 Business Objective

The main goal of this project is to help:

* Software developers understand their market value.
* Job seekers estimate expected salaries.
* Recruiters and HR teams benchmark compensation packages.
* Organizations analyze factors influencing programmer salaries.

---

## 📊 Dataset Description

The dataset contains information about programmers and software professionals, including:

| Feature          | Description                           |
| ---------------- | ------------------------------------- |
| job_title        | Current job position                  |
| experience_years | Years of professional experience      |
| education_level  | Highest educational qualification     |
| skills_count     | Number of technical skills            |
| industry         | Industry sector                       |
| company_size     | Company size category                 |
| location         | Work location                         |
| remote_work      | Remote or on-site work status         |
| certifications   | Number of professional certifications |

### Target Variable

* **Salary**

---

## 🔍 Project Workflow

### 1. Data Preprocessing

* Handling missing values
* Data cleaning
* Encoding categorical features
* Feature selection

### 2. Exploratory Data Analysis (EDA)

* Salary distribution analysis
* Experience vs Salary analysis
* Industry impact analysis
* Company size comparison
* Remote work influence

### 3. Model Development

Multiple machine learning models were tested and compared to identify the most accurate salary prediction model.

### 4. Model Evaluation

Models were evaluated using regression metrics to ensure reliable salary predictions.

### 5. Deployment

The final model was deployed using **Streamlit** to provide an interactive salary prediction web application.

---

## 📈 Key Insights

* Experience is one of the strongest factors affecting programmer salaries.
* Job title significantly influences compensation.
* Company size impacts salary ranges.
* Certifications contribute positively to salary growth.
* Remote work opportunities can affect salary expectations depending on industry and location.
* Technical skill diversity is strongly associated with higher salaries.

---

## 💡 Features

* Predict programmer salaries instantly.
* User-friendly Streamlit interface.
* Real-time salary estimation.
* Interactive input controls.
* Fast and lightweight deployment.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* XGBoost

### Visualization

* Matplotlib
* Seaborn

### Deployment

* Streamlit

## 🌐 Live Demo

Try the deployed Streamlit application and predict programmer salaries instantly:

**Live Application:**
https://programmer-salary-predictor.streamlit.app/

The web application allows users to enter programmer-related information such as:

* Job Title
* Years of Experience
* Education Level
* Skills Count
* Industry
* Company Size
* Location
* Remote Work Status
* Certifications

The model then provides an instant salary prediction based on the trained Machine Learning model.


---

## 🚀 Web Application

The project is deployed as a Streamlit web application, allowing users to enter programmer-related information and receive instant salary predictions.

---

## 📂 Project Structure

```text
Programmer-Salary-Predictor/
│
├── Programmer_Salary_Prediction.ipynb
├── Programmer_Salary_Model.pkl
├── main.py
├── requirements.txt
├── README.md
│
└── assets/
```

---

## 📊 Example Prediction

**Input:**

* Job Title: Software Engineer
* Experience: 5 Years
* Education: Bachelor's Degree
* Skills Count: 12
* Industry: Technology
* Company Size: Medium
* Location: New York
* Remote Work: Yes
* Certifications: 3

**Predicted Salary:**

* $112,000 per year

---

## 🔮 Future Improvements

* Add more salary-related features.
* Integrate real-world salary datasets.
* Support multiple countries and currencies.
* Improve prediction accuracy through advanced feature engineering.
* Add salary trend visualizations.

---

## 👨‍💻 Author

Developed as part of a Machine Learning portfolio project demonstrating data analysis, predictive modeling, and web application deployment using Streamlit.
