import streamlit as st

# -------------------------------------------------------
# Page Config
# -------------------------------------------------------

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About This Project")

st.markdown("---")

# -------------------------------------------------------
# Project Overview
# -------------------------------------------------------

st.header("🎓 Student Performance Prediction System")

st.write("""
This project predicts whether a student is likely to **PASS** or **FAIL**
using Machine Learning.

The application uses academic records, family background and
lifestyle information to estimate student performance.

The project demonstrates an end-to-end Machine Learning pipeline
with deployment using Streamlit.
""")

st.markdown("---")

# -------------------------------------------------------
# Project Workflow
# -------------------------------------------------------

st.header("🔄 Project Workflow")

st.markdown("""
1. 📂 Data Collection
2. 🧹 Data Preprocessing
3. 🤖 Model Training
4. 📈 Model Evaluation
5. 💾 Model Saving
6. 🎯 Prediction
7. 🌐 Streamlit Deployment
""")

st.markdown("---")

# -------------------------------------------------------
# Machine Learning
# -------------------------------------------------------

st.header("🤖 Machine Learning Models")

st.table({
    "Algorithm":[
        "Logistic Regression",
        "Decision Tree",
        "Random Forest"
    ],
    "Purpose":[
        "Baseline Model",
        "Tree-Based Classification",
        "Ensemble Learning"
    ]
})

st.markdown("---")

# -------------------------------------------------------
# Best Model
# -------------------------------------------------------

st.header("🏆 Best Performing Model")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Algorithm","Logistic Regression")
col2.metric("Accuracy","88.61%")
col3.metric("Precision","95.83%")
col4.metric("F1 Score","91.09%")

st.markdown("---")

# -------------------------------------------------------
# Technologies
# -------------------------------------------------------

st.header("🛠 Technologies Used")

st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Plotly
- Matplotlib
- Seaborn
- Git & GitHub
""")

st.markdown("---")

# -------------------------------------------------------
# Project Structure
# -------------------------------------------------------

st.header("📁 Project Structure")

st.code("""
Student-MLOps
│
├── app
│   ├── Home
│   ├── Prediction
│   ├── Analytics
│   └── About
│
├── artifacts
├── configs
├── data
├── notebooks
├── src
├── tests
├── monitoring
├── terraform
├── kubernetes
└── .github
""")

st.markdown("---")

# -------------------------------------------------------
# Features
# -------------------------------------------------------

st.header("✨ Project Features")

st.success("✔ Student Performance Prediction")

st.success("✔ Interactive Dashboard")

st.success("✔ Analytics Dashboard")

st.success("✔ Model Evaluation")

st.success("✔ Download Prediction Report")

st.success("✔ Machine Learning Pipeline")

st.success("✔ MLOps Ready Structure")

st.markdown("---")

# -------------------------------------------------------
# Future Scope
# -------------------------------------------------------

st.header("🚀 Future Improvements")

st.info("""
• Add Deep Learning models

• Explainable AI (SHAP)

• Real-time Prediction API

• Docker Deployment

• Kubernetes Deployment

• CI/CD Automation

• Cloud Deployment

• MLflow Integration
""")

st.markdown("---")

# -------------------------------------------------------
# Developer
# -------------------------------------------------------

st.header("👨‍💻 Developer")

st.write("""
**Student Performance Prediction System**

Developed as an academic MLOps project demonstrating:

- Data Engineering
- Machine Learning
- Model Deployment
- Streamlit Dashboard
- Software Engineering
""")

st.markdown("---")

st.caption("Student Performance Prediction System • Version 1.0")