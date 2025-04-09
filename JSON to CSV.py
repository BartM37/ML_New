import pandas as pd
import json

# Define file paths
json_file_path = "/Users/huibvanderveen/Desktop/Pycharm Projects/ML_New/YEAR/sessions_filtered_2019.json"
csv_file_path = "sessions_filtered_2019.csv"

# Read and parse JSON file
try:
    with open(json_file_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)  # Load JSON as dictionary

    # Extract the '_items' key which contains the actual data
    if '_items' in json_data:
        df = pd.DataFrame(json_data['_items'])  # Convert JSON list to DataFrame
    else:
        raise ValueError("Key '_items' not found in JSON file.")

    # Save the DataFrame to CSV
    df.to_csv(csv_file_path, index=False)
    print(f"CSV file saved successfully at: {csv_file_path}")

except FileNotFoundError:
    print("Error: JSON file not found. Ensure the file exists at the specified path.")
except json.JSONDecodeError:
    print("Error: Invalid JSON format. Check the JSON file content.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
