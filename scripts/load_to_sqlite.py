import pandas as pd
import sqlite3
import os

conn = sqlite3.connect("data/db/bluestock_mf.db")

data_path = "data/raw"

for file in os.listdir(data_path):
    if file.endswith(".csv"):

        df = pd.read_csv(os.path.join(data_path, file))

        fund_name = file.replace(".csv", "")

        df["fund_name"] = fund_name

        df.to_sql(
            "nav_history",
            conn,
            if_exists="append",
            index=False
        )

        print(f"{file} loaded")

conn.close()

print("Database created successfully")