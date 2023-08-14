import unittest
import pandas as pd
from anomalyDetection import load_data, preprocess_data, detect_anomalies

class TestAnomalyDetection(unittest.TestCase):

    def test_load_data(self):
        data = load_data("test_data.csv")  # Replace with your test data file path
        self.assertIsInstance(data, pd.DataFrame)
        self.assertTrue(len(data) > 0)

    def test_preprocess_data(self):
        data = pd.DataFrame({
            'collums_to_drop1': [1, 2, 3],
            'collums_to_drop2': [4, 5, 6],
            'numeric_attribute_1': [10, 20, 30],
            'numeric_attribute_2': [40, 50, 60],
            'categorical_attribute': ['A', 'B', 'A']
        })
        preprocessed_data = preprocess_data(data)
        self.assertIsInstance(preprocessed_data, pd.DataFrame)
        self.assertTrue('collums_to_drop1' not in preprocessed_data.columns)
        self.assertTrue('collums_to_drop2' not in preprocessed_data.columns)
        self.assertTrue('numeric_attribute_1' not in preprocessed_data.columns)
        self.assertTrue('numeric_attribute_2' not in preprocessed_data.columns)
        self.assertTrue('categorical_attribute' not in preprocessed_data.columns)
        self.assertTrue('combined_numerical_features' in preprocessed_data.columns)
        
    def test_detect_anomalies(self):
        data = pd.DataFrame({
            'numeric_attribute_1': [0.5, 1.5, 10.0, 2.0, 20.0],
            'numeric_attribute_2': [0.2, 1.2, 8.0, 1.8, 18.0],
        })
        anomalies_data = detect_anomalies(data)
        self.assertTrue('anomaly' in anomalies_data.columns)
        self.assertTrue(all(anomalies_data['anomaly'] == 1) or all(anomalies_data['anomaly'] == -1))

if __name__ == '__main__':
    unittest.main()
