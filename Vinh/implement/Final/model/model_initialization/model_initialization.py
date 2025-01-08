import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
from river import ensemble
from river import tree
from river import metrics
import joblib
import os

data_path = os.getenv("CSV_PREPROCESSED_BRIDGE")

# Load your dataset
data = pd.read_csv(data_path)
rows = data.to_dict(orient="records")

# Initialize the model
model = ensemble.BaggingClassifier(
    model=tree.HoeffdingTreeClassifier(), n_models=10, seed=27
)

# Initialize the metrics
metric = metrics.Accuracy()

for row in rows:
    X = {k: v for k, v in row.items() if k != "label"}
    y = row["label"]

    # Make prediction
    y_pred = model.predict_one(X)

    # Learn from new data
    model.learn_one(X, y)

    # Update the metric
    metric.update(y_true= y, y_pred= y_pred)

# Print the accuracy
print(f"Current accuracy score: {metric.get()}")

# Save the model and metric to files
model_filename = "model.joblib"
metric_filename = "metric.joblib"
joblib.dump(model, model_filename)
joblib.dump(metric, metric_filename)
print(f"Model and metric saved to {model_filename} and {metric_filename} respectively.")