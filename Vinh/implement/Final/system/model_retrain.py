import os
import joblib
import pandas as pd

# Function to load the old model
def loading_model(model_file = "model.joblib"):
    if os.path.exists(model_file):
        return joblib.load(model_file)
    return None

# Function to load the old metric
def loading_metric(metric_file = "metric.joblib"):
    if os.path.exists(metric_file):
        return joblib.load(metric_file)
    return None

# Function to save new model
def saving_model(model, model_file = "model.joblib"):
    joblib.dump(model, model_file)

# Function to save new metric
def saving_metric(metric, metric_file = "metric.joblib"):
    joblib.dump(metric, metric_file)

# Function to retrain model for new file
def process(input_file, model, metric):
    # Loading data
    data = pd.read_csv(input_file)
    rows = data.to_dict(orient= "records")

    for row in rows:
        X = {k: v for k, v in row.items() if k != "label"}
        y = row["label"]

        # Making prediction for each row
        y_pred = model.predict_one(X)

        # Learning new data point
        model.learn_one(X, y)

        # Updating the current accuracy
        metric.update(y_true = y, y_pred = y_pred)
    
    # Print the accuracy
    print(f"Current accuracy score: {metric.get()}")

model = loading_model(model_file="model.joblib")
metric = loading_metric(metric_file="metric.joblib")

input_file = os.getenv("FILE")
process(input_file= input_file, model= model, metric= metric)



