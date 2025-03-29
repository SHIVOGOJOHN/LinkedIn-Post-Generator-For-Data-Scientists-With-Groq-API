import json
import re

# Path to your JSON file
input_path = r"C:\Users\A\.vscode\.vscode\LinkedIn\jsononline-net.json"  # Replace with your actual file path
output_path = r'C:\Users\A\.vscode\.vscode\LinkedIn\reformatted_json.json'

# Step 1: Read the raw data
with open(input_path, 'r', encoding='utf-8') as file:
    raw_data = file.read()

# Step 2: Use regex to remove problematic escape sequences
# Replace invalid escape sequences that aren't followed by valid unicode characters
cleaned_data_str = re.sub(r'\\[^\\"bfnrtu]', '', raw_data)

print("Raw data read successfully.")
print("After cleaning, data length:", len(cleaned_data_str))

# Step 3: Parse and reformat the JSON data
try:
    cleaned_data = json.loads(cleaned_data_str)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)
    print("JSON file saved successfully.")
except json.JSONDecodeError as e:
    print("JSON decoding error:", e)
except Exception as e:
    print("An error occurred:", e)