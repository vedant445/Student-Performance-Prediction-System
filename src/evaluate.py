import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


class ModelEvaluation:

    def __init__(self):

        self.model_path = "artifacts/model.pkl"

        self.X_test_path = "data/processed/X_test.csv"
        self.y_test_path = "data/processed/y_test.csv"

    def evaluate(self):

        # -------------------------
        # Load Model
        # -------------------------

        model = joblib.load(self.model_path)

        # -------------------------
        # Load Test Data
        # -------------------------

        X_test = pd.read_csv(self.X_test_path)
        y_test = pd.read_csv(self.y_test_path).values.ravel()

        # -------------------------
        # Prediction
        # -------------------------

        predictions = model.predict(X_test)

        # -------------------------
        # Metrics
        # -------------------------

        accuracy = accuracy_score(y_test, predictions)
        precision = precision_score(y_test, predictions)
        recall = recall_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)

        print("=" * 50)
        print("MODEL EVALUATION")
        print("=" * 50)

        print(f"\nAccuracy : {accuracy:.4f}")
        print(f"Precision: {precision:.4f}")
        print(f"Recall   : {recall:.4f}")
        print(f"F1 Score : {f1:.4f}")

        print("\nConfusion Matrix")
        print(confusion_matrix(y_test, predictions))

        print("\nClassification Report")
        print(classification_report(y_test, predictions))


if __name__ == "__main__":

    evaluator = ModelEvaluation()
    evaluator.evaluate()