import os
import pandas as pd

# Function to calculate accuracy
def accuracy_calculate(true_file, predict_file):
    try:
        # Reading data
        true_data = pd.read_csv(true_file)
        predict_data = pd.read_csv(predict_file)

        # Extract label column
        true_column = true_data["label"]
        predict_column = predict_data["label"]

        if len(true_column) == len(predict_column):
            matches = (true_column == predict_column).sum()
            total = len(true_column)
            accuracy = matches / total
            return accuracy * 100
    except Exception as e:
        print(f"Error: {e}")

# Function to find symmetric predicted file by model
def find_symmetric_predicted_data(labeled_file_name):
    symmetric_predicted_file_name = f"predicted_{labeled_file_name}"
    return symmetric_predicted_file_name

if __name__ == "__main__":
    labeled_file_name = os.getenv("FILE")
    symmetric_predicted_file_name = find_symmetric_predicted_data(labeled_file_name)

    accuracy_score = accuracy_calculate(true_file= labeled_file_name, predict_file= symmetric_predicted_file_name)
    print(f"{accuracy_score:.2f}")




        


