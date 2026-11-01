import streamlit as st

st.set_page_config(page_title="Student Performance Prediction", page_icon="🎓")

st.title("🎓 Student Performance Prediction System")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("📌 Project Overview")

    st.write("""
This application predicts whether a student is likely to **PASS** or **FAIL**
using Machine Learning.

The project demonstrates a complete MLOps pipeline including:

- 📥 Data Ingestion
- 🧹 Data Preprocessing
- 🤖 Model Training
- 📊 Model Evaluation
- 💾 Model Saving
- 🌐 Streamlit Deployment
    """)

with col2:
    st.header("📈 Model Performance")

    st.metric("Accuracy", "88.61%")
    st.metric("Precision", "95.83%")
    st.metric("Recall", "86.79%")
    st.metric("F1 Score", "91.09%")

st.markdown("---")

st.subheader("📂 Dataset")

st.info("""
Dataset: Student Performance Dataset (UCI Machine Learning Repository)

The model uses:

• Academic Information

• Family Background

• Lifestyle Habits

to predict the student's final outcome.
""")

st.markdown("---")

st.subheader("🚀 Workflow")

st.write("""
1. Load Student Data

⬇

2. Preprocess Features

⬇

3. Train Multiple Models

⬇

4. Select Best Model

⬇

5. Save Model

⬇

6. Predict PASS / FAIL
""")

st.markdown("---")

st.success("👉 Use the Prediction page from the sidebar to test the model.")