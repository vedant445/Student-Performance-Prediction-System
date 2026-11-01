import joblib
import pandas as pd


class StudentPredictor:

    def __init__(self):

        self.model = joblib.load("artifacts/model.pkl")

    def predict(self, student):

        df = pd.DataFrame([student])

        prediction = self.model.predict(df)[0]

        if prediction == 1:
            return "PASS"
        else:
            return "FAIL"


if __name__ == "__main__":

    predictor = StudentPredictor()

    student = {

        "age": 17,
        "Medu": 4,
        "Fedu": 4,
        "traveltime": 2,
        "studytime": 3,
        "failures": 0,
        "famrel": 4,
        "freetime": 3,
        "goout": 3,
        "Dalc": 1,
        "Walc": 1,
        "health": 5,
        "absences": 2,
        "G1": 15,
        "G2": 14,

        "school_MS": 0,
        "sex_M": 1,
        "address_U": 1,
        "famsize_LE3": 0,
        "Pstatus_T": 1,

        "Mjob_health": 0,
        "Mjob_other": 0,
        "Mjob_services": 1,
        "Mjob_teacher": 0,

        "Fjob_health": 0,
        "Fjob_other": 1,
        "Fjob_services": 0,
        "Fjob_teacher": 0,

        "reason_home": 0,
        "reason_other": 0,
        "reason_reputation": 1,

        "guardian_mother": 1,
        "guardian_other": 0,

        "schoolsup_yes": 0,
        "famsup_yes": 1,
        "paid_yes": 0,
        "activities_yes": 1,
        "nursery_yes": 1,
        "higher_yes": 1,
        "internet_yes": 1,
        "romantic_yes": 0
    }

    result = predictor.predict(student)

    print("=" * 40)
    print("Student Performance Prediction")
    print("=" * 40)
    print("Prediction :", result)