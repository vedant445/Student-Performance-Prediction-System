import os
import joblib
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


class ModelTraining:

    def __init__(self):

        self.X_train_path = "data/processed/X_train.csv"
        self.X_test_path = "data/processed/X_test.csv"
        self.y_train_path = "data/processed/y_train.csv"
        self.y_test_path = "data/processed/y_test.csv"

        self.model_path = "artifacts/model.pkl"

    def train_model(self):

        X_train = pd.read_csv(self.X_train_path)
        X_test = pd.read_csv(self.X_test_path)

        y_train = pd.read_csv(self.y_train_path).values.ravel()
        y_test = pd.read_csv(self.y_test_path).values.ravel()

        models = {

            "Logistic Regression":
                LogisticRegression(max_iter=1000),

            "Decision Tree":
                DecisionTreeClassifier(random_state=42),

            "Random Forest":
                RandomForestClassifier(
                    n_estimators=100,
                    random_state=42
                )

        }

        best_model = None
        best_accuracy = 0

        print("=" * 50)
        print("TRAINING MODELS")
        print("=" * 50)

        for name, model in models.items():

            model.fit(X_train, y_train)

            prediction = model.predict(X_test)

            accuracy = accuracy_score(y_test, prediction)
            precision = precision_score(y_test, prediction)
            recall = recall_score(y_test, prediction)
            f1 = f1_score(y_test, prediction)

            print(f"\n{name}")
            print(f"Accuracy : {accuracy:.4f}")
            print(f"Precision: {precision:.4f}")
            print(f"Recall   : {recall:.4f}")
            print(f"F1 Score : {f1:.4f}")

            if accuracy > best_accuracy:

                best_accuracy = accuracy
                best_model = model

        os.makedirs("artifacts", exist_ok=True)

        joblib.dump(best_model, self.model_path)

        print("\n" + "=" * 50)
        print("TRAINING COMPLETED")
        print("=" * 50)
        print(f"Best Accuracy : {best_accuracy:.4f}")
        print(f"Model Saved : {self.model_path}")


if __name__ == "__main__":

    trainer = ModelTraining()
    trainer.train_model()