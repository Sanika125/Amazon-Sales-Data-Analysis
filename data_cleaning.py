import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, low_memory=False)

    # Remove unwanted columns
    df = df.drop(columns=["Unnamed: 22", "index"], errors="ignore")

    # Convert data types
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

    # Remove invalid rows
    df = df.dropna(subset=["Amount"])
    df = df[df["Amount"] > 0]

    return df