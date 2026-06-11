import pandas as pd
import os

data_path = "data/raw"

files = [f for f in os.listdir(data_path) if f.endswith(".csv")]

for file in files:
    print("=" * 60)
    print("Dataset:", file)

    df = pd.read_csv(os.path.join(data_path, file))

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())