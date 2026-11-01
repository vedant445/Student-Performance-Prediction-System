import joblib
import pandas as pd

# -------------------------
# Load Model
# -------------------------

MODEL_PATH = "artifacts/model.pkl"

model = joblib.load(MODEL_PATH)


# -------------------------
# Prediction Function
# -------------------------

def predict_student(data):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    probability = model.predict_proba(df)[0]

    confidence = round(max(probability) * 100, 2)

    result = "PASS" if prediction == 1 else "FAIL"

    return result, confidence


# -------------------------
# Risk Level
# -------------------------

def risk_level(confidence):

    if confidence >= 90:
        return "🟢 Low Risk"

    elif confidence >= 75:
        return "🟡 Medium Risk"

    else:
        return "🔴 High Risk"


# -------------------------
# Recommendation
# -------------------------

def recommendation(result):

    if result == "PASS":

        return [
            "Continue your current study routine.",
            "Maintain attendance.",
            "Keep G2 performance consistent.",
            "Practice regularly before exams."
        ]

    else:

        return [
            "Increase daily study time.",
            "Reduce absenteeism.",
            "Seek teacher or mentor support.",
            "Focus on improving G1 and G2 scores."
        ]


# -------------------------
# Student Summary
# -------------------------

def summary(data):

    return pd.DataFrame({

        "Feature": [

            "Age",
            "Study Time",
            "Previous Failures",
            "G1",
            "G2",
            "Absences",
            "Health"

        ],

        "Value": [

            data["age"],
            data["studytime"],
            data["failures"],
            data["G1"],
            data["G2"],
            data["absences"],
            data["health"]

        ]

    })


# -------------------------
# Model Metrics
# -------------------------

MODEL_METRICS = {

    "Accuracy": 88.61,
    "Precision": 95.83,
    "Recall": 86.79,
    "F1 Score": 91.09

}