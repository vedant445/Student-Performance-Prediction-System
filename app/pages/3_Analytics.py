import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------------
# Page Config
# -------------------------------------------------------

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Performance Analytics")

st.write(
    "Explore the dataset, model performance and student statistics."
)

st.markdown("---")

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/student.csv")

df = load_data()

# -------------------------------------------------------
# Detect Target Column
# -------------------------------------------------------

target = None

for col in ["pass", "Pass", "target", "Target", "Result", "result"]:
    if col in df.columns:
        target = col
        break

# -------------------------------------------------------
# KPI Cards
# -------------------------------------------------------

students = len(df)
features = len(df.columns)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Students", students)
col2.metric("Features", features)
col3.metric("Missing Values", int(df.isnull().sum().sum()))
col4.metric("Duplicate Rows", int(df.duplicated().sum()))

st.markdown("---")

# -------------------------------------------------------
# Dataset Preview
# -------------------------------------------------------

st.subheader("📋 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

st.markdown("---")

# -------------------------------------------------------
# Dataset Statistics
# -------------------------------------------------------

st.subheader("📈 Dataset Statistics")

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.markdown("---")

# -------------------------------------------------------
# Pass vs Fail
# -------------------------------------------------------

if target is not None:

    st.subheader("🎓 Pass vs Fail Distribution")

    fig = px.histogram(
        df,
        x=target,
        color=target,
        text_auto=True
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

# -------------------------------------------------------
# Grade Distribution
# -------------------------------------------------------

grade_columns = []

for col in ["G1", "G2"]:

    if col in df.columns:
        grade_columns.append(col)

if len(grade_columns) > 0:

    st.subheader("📚 Grade Distribution")

    fig = px.histogram(
        df,
        x=grade_columns[0],
        nbins=20
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    if len(grade_columns) == 2:

        fig = px.histogram(
            df,
            x=grade_columns[1],
            nbins=20
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

st.markdown("---")

# -------------------------------------------------------
# Correlation Heatmap
# -------------------------------------------------------

st.subheader("🔥 Correlation Heatmap")

numeric_df = df.select_dtypes(include="number")

corr = numeric_df.corr()

fig, ax = plt.subplots(figsize=(12,8))

sns.heatmap(
    corr,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)

st.markdown("---")

# -------------------------------------------------------
# Feature Importance (Correlation)
# -------------------------------------------------------

if target is not None:

    st.subheader("🏆 Feature Importance")

    correlations = corr[target].drop(target)

    correlations = correlations.abs()

    correlations = correlations.sort_values(
        ascending=False
    )

    top = correlations.head(10)

    fig = px.bar(
        x=top.values,
        y=top.index,
        orientation="h",
        labels={
            "x":"Correlation",
            "y":"Feature"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

# -------------------------------------------------------
# Student Age Distribution
# -------------------------------------------------------

if "age" in df.columns:

    st.subheader("🎂 Age Distribution")

    fig = px.histogram(
        df,
        x="age",
        nbins=10
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# -------------------------------------------------------
# Study Time
# -------------------------------------------------------

if "studytime" in df.columns:

    st.subheader("📖 Study Time")

    fig = px.pie(
        df,
        names="studytime"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# -------------------------------------------------------
# Absence Distribution
# -------------------------------------------------------

if "absences" in df.columns:

    st.subheader("🚫 Absence Distribution")

    fig = px.box(
        df,
        y="absences"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# -------------------------------------------------------
# Download Dataset
# -------------------------------------------------------

st.subheader("📥 Download Dataset")

csv = df.to_csv(index=False)

st.download_button(
    label="Download Dataset",
    data=csv,
    file_name="student_dataset.csv",
    mime="text/csv",
    use_container_width=True
)

st.markdown("---")

st.success("✅ Analytics Dashboard Loaded Successfully")