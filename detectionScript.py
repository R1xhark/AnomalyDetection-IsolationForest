import argparse
import pandas as pd
from sklearn.ensemble import IsolationForest

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
   #in progress
    return data

def detect_anomalies(data):
    model = IsolationForest(contamination=0.05)
    data['anomaly'] = model.fit_predict(data)
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=str, help="Path to the CSV file containing security data")
    args = parser.parse_args()

    file_path = args.file_path
    data = load_data(file_path)
    print("Original Data:")
    print(data.head())

    data = preprocess_data(data)
    print("\nPreprocessed Data:")
    print(data.head())

    data = detect_anomalies(data)
    anomalies = data[data['anomaly'] == -1]
    print("\nAnomalies Detected:")
    print(anomalies)
