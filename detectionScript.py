import argparse
import pandas as pd
from sklearn.ensemble import IsolationForest

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    collums_to_drop = ['collums_to_drop1', 'collums_to_drop2']
    data = data.drop(columns=collums_to_drop)
    
    data.fillna(0, inplace=True)

    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    numerické_sloupce = ['numeric_attribute_1', 'numeric_attribute_2']
    data[numerické_sloupce] = scaler.fit_transform(data[numerické_sloupce])

    kategorické_sloupce = ['categorical_attribute']
    data = pd.get_dummies(data, columns=categorical_attribute, drop_first=True)

    data['nový_příznak'] = data['numeric_attribute_1'] + data['numeric_attribute_1']

    return data

def detect_anomalies(data):
    model = IsolationForest(contamination=0.05)
    data['anomaly'] = model.fit_predict(data)
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", type=str, help="Cesta k CSV souboru obsahujícímu bezpečnostní data")
    args = parser.parse_args()

    file_path = args.file_path
    data = load_data(file_path)
    print("Původní Data:")
    print(data.head())

    data = preprocess_data(data)
    print("\nZpracovaná Data:")
    print(data.head())

    data = detect_anomalies(data)
    anomalies = data[data['anomaly'] == -1]
    print("\nDetekované Anomalie:")
    print(anomalies)

