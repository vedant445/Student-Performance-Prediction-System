import os
import pandas as pd

from sklearn.model_selection import train_test_split


class DataPreprocessing:

    def __init__(self):

        self.input_path = "data/processed/student.csv"
        self.output_path = "data/processed"

    def preprocess_data(self):

        # -------------------------
        # Load Dataset
        # -------------------------

        if not os.path.exists(self.input_path):
            raise FileNotFoundError(
                f"{self.input_path} not found."
            )

        df = pd.read_csv(self.input_path)

        print("=" * 50)
        print("Original Dataset")
        print("=" * 50)
        print(df.head())

        # -------------------------
        # Missing Values
        # -------------------------

        print("\nChecking Missing Values...\n")

        print(df.isnull().sum())

        # -------------------------
        # Create Target Variable
        # -------------------------

        # Pass = 1
        # Fail = 0

        df["Pass"] = df["G3"].apply(
            lambda x: 1 if x >= 10 else 0
        )

        # -------------------------
        # Drop G3
        # -------------------------

        df.drop("G3", axis=1, inplace=True)

        # -------------------------
        # One Hot Encoding
        # -------------------------

        df = pd.get_dummies(
            df,
            drop_first=True
        )

        # -------------------------
        # Features & Target
        # -------------------------

        X = df.drop("Pass", axis=1)

        y = df["Pass"]

        # -------------------------
        # Train Test Split
        # -------------------------

        X_train, X_test, y_train, y_test = train_test_split(

            X,
            y,

            test_size=0.20,

            random_state=42,

            stratify=y

        )

        # -------------------------
        # Save Processed Files
        # -------------------------

        os.makedirs(
            self.output_path,
            exist_ok=True
        )

        X_train.to_csv(
            f"{self.output_path}/X_train.csv",
            index=False
        )

        X_test.to_csv(
            f"{self.output_path}/X_test.csv",
            index=False
        )

        y_train.to_csv(
            f"{self.output_path}/y_train.csv",
            index=False
        )

        y_test.to_csv(
            f"{self.output_path}/y_test.csv",
            index=False
        )

        print("\n" + "=" * 50)
        print("Preprocessing Completed Successfully")
        print("=" * 50)

        print(f"\nTraining Samples : {len(X_train)}")
        print(f"Testing Samples  : {len(X_test)}")

        print("\nSaved Files")

        print("--------------------------")

        print("X_train.csv")
        print("X_test.csv")
        print("y_train.csv")
        print("y_test.csv")

        return X_train, X_test, y_train, y_test


if __name__ == "__main__":

    preprocess = DataPreprocessing()

    preprocess.preprocess_data()