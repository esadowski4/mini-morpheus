# detect.py
import pandas as pd
from sklearn.ensemble import IsolationForest

# 100 "normal" packets (size 50-150) and 5 "anomalous" packets (size 500-600)
normal_data = pd.DataFrame({'length': [i for i in range(50, 150)]})
anomalous_data = pd.DataFrame({'length': [500, 550, 525, 600, 575]})
training_data = pd.concat([normal_data, anomalous_data])

# Initialize the Model
# Contamination is the expected % of anomalies in data.
model = IsolationForest(contamination=0.05, random_state=42)

# Train the Model
model.fit(training_data[['length']])

# Make Predictions
# The model returns 1 for normal (inlier) and -1 for anomalous (outlier)
predictions = model.predict(training_data[['length']])
training_data['anomaly'] = predictions

print("Prediction Results:")
print(training_data)

print("\nAnomalies Detected:")
print(training_data[training_data['anomaly'] == -1])