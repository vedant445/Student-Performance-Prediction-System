import os
import pandas as pd


class DataIngestion:

    def __init__(self):
        self.raw_path = "data/raw/student-mat.csv"
        self.processed_path = "data/processed/student.csv"

    def load_data(self):

        if not os.path.exists(self.raw_path):
            raise FileNotFoundError(
                f"Dataset not found at {self.raw_path}"
            )

        df = pd.read_csv(self.raw_path, sep=";")

        if df.empty:
            raise ValueError("Dataset is empty.")

        os.makedirs("data/processed", exist_ok=True)

        df.to_csv(self.processed_path, index=False)

        print("=" * 50)
        print("Data Loaded Successfully")
        print("=" * 50)
        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")
        print(f"Saved   : {self.processed_path}")

        return df


if __name__ == "__main__":
    ingestion = DataIngestion()
    data = ingestion.load_data()

    print("\nFirst Five Rows\n")
    print(data.head())