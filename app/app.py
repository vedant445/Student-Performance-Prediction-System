import streamlit as st
from style import load_css

# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------
# Load Custom CSS
# -------------------------

load_css()

# -------------------------
# Sidebar
# -------------------------

st.sidebar.title("🎓 Student Performance")
st.sidebar.markdown("---")

st.sidebar.success("Navigation")

st.sidebar.info(
    """
    📄 Home

    🎯 Prediction

    📊 Analytics

    ℹ️ About
    """
)

st.sidebar.markdown("---")

st.sidebar.write("### Model")

st.sidebar.write("✔ Logistic Regression")

st.sidebar.write("Accuracy : **88.61%**")

st.sidebar.markdown("---")

st.sidebar.write("Made with ❤️ using")

st.sidebar.write("""
- Streamlit
- Scikit-Learn
- Pandas
- Joblib
""")

# -------------------------
# Home Screen
# -------------------------

st.title("🎓 Student Performance Prediction System")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.header("📌 Project Overview")

    st.write("""
This application predicts whether a student is likely to **PASS** or **FAIL**
based on academic performance, family background and lifestyle information.

The project demonstrates a complete Machine Learning pipeline including:

- Data Ingestion
- Data Preprocessing
- Model Training
- Model Evaluation
- Prediction
- Docker Ready
- Kubernetes Ready
- Prometheus Monitoring
""")

with col2:

    st.header("📈 Model Performance")

    c1, c2 = st.columns(2)

    c1.metric("Accuracy", "88.61%")
    c2.metric("Precision", "95.83%")

    c3, c4 = st.columns(2)

    c3.metric("Recall", "86.79%")
    c4.metric("F1 Score", "91.09%")

st.markdown("---")

st.success("👈 Use the pages in the left sidebar to explore the application.")