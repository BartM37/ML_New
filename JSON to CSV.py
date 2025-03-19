import pandas as pd
import json

# Define the correct file paths
json_file_path = "acndata_sessions.json"  # Ensure this path is correct
csv_file_path = "acndata_sessions.csv"

# Read the JSON file properly
try:
    with open(json_file_path, "r", encoding="utf-8") as file:
        json_data = json.load(file)  # Load JSON as dictionary

    # Extract the '_items' key which contains the actual data
    if '_items' in json_data:
        df = pd.DataFrame(json_data['_items'])  # Convert JSON list to DataFrame
    else:
        df = pd.DataFrame(json_data)  # Fallback if '_items' key is missing

    # Save the DataFrame to CSV
    df.to_csv(csv_file_path, index=False)
    print(f"CSV file saved successfully at: {csv_file_path}")

except FileNotFoundError:
    print("Error: JSON file not found. Ensure the file exists at the specified path.")
except json.JSONDecodeError:
    print("Error: Invalid JSON format. Check the JSON file content.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
