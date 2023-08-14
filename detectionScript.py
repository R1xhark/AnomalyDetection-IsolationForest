import argparse
import pandas as pd
from sklearn.ensemble import IsolationForest

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    columns_to_drop = ['column_to_drop1', 'column_to_drop2']
    data = data.drop(columns=columns_to_drop)
    
    data.fillna(0, inplace=True)

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    numeric_columns = ['numeric_attribute_1', 'numeric_attribute_2']
    data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

    categorical_columns = ['categorical_attribute']
    data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

    data['combined_numeric_features'] = data['numeric_attribute_1'] + data['numeric_attribute_2']

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
