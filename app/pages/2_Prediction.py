import streamlit as st
import pandas as pd
import joblib
import numpy as np

# -------------------------------------------------
# Page Config
# -------------------------------------------------

st.set_page_config(
    page_title="Prediction",
    page_icon="🎯",
    layout="wide"
)

# -------------------------------------------------
# Load Model
# -------------------------------------------------

@st.cache_resource
def load_model():
    return joblib.load("artifacts/model.pkl")

model = load_model()

st.title("🎯 Student Performance Prediction")

st.write(
    "Fill in the student's details below and click **Predict**."
)

st.markdown("---")

# =====================================================
# Academic Information
# =====================================================

st.header("📚 Academic Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 15, 22, 17)

    studytime = st.slider(
        "Study Time",
        1,
        4,
        2
    )

    failures = st.slider(
        "Previous Failures",
        0,
        4,
        0
    )

with col2:
    G1 = st.slider(
        "First Period Grade (G1)",
        0,
        20,
        12
    )

    G2 = st.slider(
        "Second Period Grade (G2)",
        0,
        20,
        12
    )

    absences = st.slider(
        "Absences",
        0,
        50,
        5
    )

with col3:

    Medu = st.selectbox(
        "Mother Education",
        [0,1,2,3,4],
        index=2
    )

    Fedu = st.selectbox(
        "Father Education",
        [0,1,2,3,4],
        index=2
    )

    traveltime = st.selectbox(
        "Travel Time",
        [1,2,3,4],
        index=0
    )

st.markdown("---")

# =====================================================
# Family
# =====================================================

st.header("🏠 Family Information")

col1, col2 = st.columns(2)

with col1:

    famrel = st.slider(
        "Family Relationship",
        1,
        5,
        4
    )

    freetime = st.slider(
        "Free Time",
        1,
        5,
        3
    )

    goout = st.slider(
        "Going Out",
        1,
        5,
        3
    )

with col2:

    Dalc = st.slider(
        "Weekday Alcohol",
        1,
        5,
        1
    )

    Walc = st.slider(
        "Weekend Alcohol",
        1,
        5,
        2
    )

    health = st.slider(
        "Health",
        1,
        5,
        4
    )

st.markdown("---")

# =====================================================
# Additional Information
# =====================================================

st.header("📝 Additional Information")

col1, col2 = st.columns(2)

with col1:

    school = st.selectbox(
        "School",
        ["GP","MS"]
    )

    sex = st.selectbox(
        "Gender",
        ["Female","Male"]
    )

    address = st.selectbox(
        "Address",
        ["Urban","Rural"]
    )

    famsize = st.selectbox(
        "Family Size",
        ["GT3","LE3"]
    )

    Pstatus = st.selectbox(
        "Parents Status",
        ["Together","Apart"]
    )

    guardian = st.selectbox(
        "Guardian",
        ["Mother","Father","Other"]
    )

with col2:

    Mjob = st.selectbox(
        "Mother Job",
        [
            "at_home",
            "health",
            "other",
            "services",
            "teacher"
        ]
    )

    Fjob = st.selectbox(
        "Father Job",
        [
            "at_home",
            "health",
            "other",
            "services",
            "teacher"
        ]
    )

    reason = st.selectbox(
        "Reason",
        [
            "course",
            "home",
            "other",
            "reputation"
        ]
    )

    schoolsup = st.selectbox(
        "School Support",
        ["No","Yes"]
    )

    famsup = st.selectbox(
        "Family Support",
        ["No","Yes"]
    )

    paid = st.selectbox(
        "Paid Classes",
        ["No","Yes"]
    )

activities = st.selectbox(
    "Activities",
    ["No","Yes"]
)

nursery = st.selectbox(
    "Nursery",
    ["No","Yes"]
)

higher = st.selectbox(
    "Higher Education",
    ["No","Yes"]
)

internet = st.selectbox(
    "Internet",
    ["No","Yes"]
)

romantic = st.selectbox(
    "Romantic Relationship",
    ["No","Yes"]
)

st.markdown("---")

predict = st.button(
    "🚀 Predict Student Performance",
    use_container_width=True
)
# =====================================================
# Prediction
# =====================================================

if predict:

    input_data = {
        "age": age,
        "Medu": Medu,
        "Fedu": Fedu,
        "traveltime": traveltime,
        "studytime": studytime,
        "failures": failures,
        "famrel": famrel,
        "freetime": freetime,
        "goout": goout,
        "Dalc": Dalc,
        "Walc": Walc,
        "health": health,
        "absences": absences,
        "G1": G1,
        "G2": G2,

        "school_MS": 1 if school == "MS" else 0,
        "sex_M": 1 if sex == "Male" else 0,
        "address_U": 1 if address == "Urban" else 0,
        "famsize_LE3": 1 if famsize == "LE3" else 0,
        "Pstatus_T": 1 if Pstatus == "Together" else 0,

        "Mjob_health": 1 if Mjob == "health" else 0,
        "Mjob_other": 1 if Mjob == "other" else 0,
        "Mjob_services": 1 if Mjob == "services" else 0,
        "Mjob_teacher": 1 if Mjob == "teacher" else 0,

        "Fjob_health": 1 if Fjob == "health" else 0,
        "Fjob_other": 1 if Fjob == "other" else 0,
        "Fjob_services": 1 if Fjob == "services" else 0,
        "Fjob_teacher": 1 if Fjob == "teacher" else 0,

        "reason_home": 1 if reason == "home" else 0,
        "reason_other": 1 if reason == "other" else 0,
        "reason_reputation": 1 if reason == "reputation" else 0,

        "guardian_mother": 1 if guardian == "Mother" else 0,
        "guardian_other": 1 if guardian == "Other" else 0,

        "schoolsup_yes": 1 if schoolsup == "Yes" else 0,
        "famsup_yes": 1 if famsup == "Yes" else 0,
        "paid_yes": 1 if paid == "Yes" else 0,
        "activities_yes": 1 if activities == "Yes" else 0,
        "nursery_yes": 1 if nursery == "Yes" else 0,
        "higher_yes": 1 if higher == "Yes" else 0,
        "internet_yes": 1 if internet == "Yes" else 0,
        "romantic_yes": 1 if romantic == "Yes" else 0,
    }

    df = pd.DataFrame([input_data])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0]

    confidence = np.max(probability) * 100

    st.markdown("---")

    st.header("📊 Prediction Result")

    if prediction == 1:

        st.success("## ✅ PASS")

        risk = "🟢 LOW RISK"

        recommendation = [
            "Continue the current study routine.",
            "Maintain attendance.",
            "Keep preparing consistently.",
            "Attempt previous year papers."
        ]

    else:

        st.error("## ❌ FAIL")

        risk = "🔴 HIGH RISK"

        recommendation = [
            "Increase daily study hours.",
            "Reduce unnecessary outings.",
            "Attend remedial classes.",
            "Improve G1 and G2 scores.",
            "Take help from teachers."
        ]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Prediction",
            "PASS" if prediction == 1 else "FAIL"
        )

    with col2:
        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

    with col3:
        st.metric(
            "Risk Level",
            risk
        )

    st.markdown("---")

    st.subheader("📈 Prediction Probability")

    st.write("PASS Probability")

    st.progress(float(probability[1]))

    st.write(f"{probability[1]*100:.2f}%")

    st.write("FAIL Probability")

    st.progress(float(probability[0]))

    st.write(f"{probability[0]*100:.2f}%")

    st.markdown("---")

    st.subheader("💡 Recommendations")

    for item in recommendation:
        st.write("✔", item)

    st.markdown("---")

    st.subheader("📋 Student Summary")

    c1, c2 = st.columns(2)

    with c1:
        st.write("Age:", age)
        st.write("Study Time:", studytime)
        st.write("Failures:", failures)
        st.write("G1:", G1)
        st.write("G2:", G2)

    with c2:
        st.write("Absences:", absences)
        st.write("Health:", health)
        st.write("Free Time:", freetime)
        st.write("Going Out:", goout)
        st.write("School:", school)

    # =====================================================
    # Prediction Insights
    # =====================================================

    st.markdown("---")

    st.subheader("📈 Performance Indicators")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Academic Score",
            value=f"{((G1 + G2) / 40) * 100:.1f}%"
        )

    with col2:
        st.metric(
            label="Attendance",
            value=f"{max(0, 100 - absences * 2)}%"
        )

    with col3:
        st.metric(
            label="Study Level",
            value=f"{studytime}/4"
        )

    st.markdown("---")

    st.subheader("📊 Student Dashboard")

    dashboard = pd.DataFrame(
        {
            "Feature": [
                "Age",
                "Study Time",
                "Failures",
                "Absences",
                "Health",
                "Free Time",
                "Going Out",
                "Weekday Alcohol",
                "Weekend Alcohol",
                "Family Relation"
            ],
            "Value": [
                age,
                studytime,
                failures,
                absences,
                health,
                freetime,
                goout,
                Dalc,
                Walc,
                famrel
            ]
        }
    )

    st.dataframe(
        dashboard,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    st.subheader("🤖 Model Information")

    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Algorithm", "Logistic Regression")
    m2.metric("Accuracy", "88.61%")
    m3.metric("Precision", "95.83%")
    m4.metric("F1 Score", "91.09%")

    st.markdown("---")

    st.subheader("📝 Prediction Explanation")

    if prediction == 1:

        st.success(
            """
    The student is predicted to PASS because the academic indicators
    (G1, G2, study time and failures) suggest a good overall performance.

    Continue maintaining study habits and attendance.
    """
        )

    else:

        st.error(
            """
    The student is predicted to FAIL because one or more academic
    factors indicate risk.

    Improving G1, G2 and reducing absences will significantly
    increase the probability of passing.
    """
        )

    st.markdown("---")

    st.subheader("📄 Download Prediction Report")

    report = pd.DataFrame({
        "Parameter": [
            "Prediction",
            "Confidence",
            "Risk Level",
            "Age",
            "Study Time",
            "Failures",
            "G1",
            "G2",
            "Absences"
        ],
        "Value": [
            "PASS" if prediction == 1 else "FAIL",
            f"{confidence:.2f}%",
            risk,
            age,
            studytime,
            failures,
            G1,
            G2,
            absences
        ]
    })

    csv = report.to_csv(index=False)

    st.download_button(
        label="📥 Download Prediction Report",
        data=csv,
        file_name="student_prediction_report.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.markdown("---")

    st.caption("Student Performance Prediction System • MLOps Project")