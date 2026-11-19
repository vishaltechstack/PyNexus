# ==============================================================================
# FILE: 15_csv_and_json.py
# TOPIC: Reading & Writing CSV (DictReader/DictWriter) and JSON Files
# ==============================================================================

import csv
import json
from pathlib import Path

workspace = Path("sample_workspace")
workspace.mkdir(exist_ok=True)

# ==============================================================================
# PART A: CSV PROCESSING (Tabular Data)
# ==============================================================================
csv_path = workspace / "test_data.csv"

test_rows = [
    {"test_id": "TC_01", "module": "Auth", "status": "PASS", "time_sec": 1.4},
    {"test_id": "TC_02", "module": "Cart", "status": "FAIL", "time_sec": 4.8},
    {"test_id": "TC_03", "module": "Payment", "status": "PASS", "time_sec": 2.1},
]

# 1. Writing dictionaries to CSV using csv.DictWriter
# NOTE: Always pass newline="" on Windows when opening CSV files to avoid blank rows!
fieldnames = ["test_id", "module", "status", "time_sec"]

with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()                          # Writes column headers in row 1
    writer.writerows(test_rows)                   # Writes all dictionaries as rows

# 2. Reading CSV back as dictionaries using csv.DictReader
print("=== Reading CSV Rows ===")
with open(csv_path, mode="r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Each 'row' is a dictionary where column headers are keys (all values are strings)
        print(f"  {row['test_id']} [{row['module']}] -> {row['status']} ({row['time_sec']}s)")

# ==============================================================================
# PART B: JSON PROCESSING (Nested API & Config Data)
# ==============================================================================
json_path = workspace / "suite_config.json"

config_data = {
    "project": "Vtiger_CRM_Automation",
    "browser": "chromium",
    "headless": True,
    "retries": 2,
    "tags": ["smoke", "regression"],
    "credentials": None                           # Converts to 'null' in JSON
}

# 1. Python Dict -> JSON File (json.dump) & JSON String (json.dumps)
# indent=4 formats the JSON cleanly for human readability.
with open(json_path, mode="w", encoding="utf-8") as f:
    json.dump(config_data, f, indent=4)

json_string = json.dumps(config_data)             # Serializes to an in-memory string

# 2. JSON File -> Python Dict (json.load) & JSON String -> Python Dict (json.loads)
with open(json_path, mode="r", encoding="utf-8") as f:
    loaded_config = json.load(f)

print("\n=== Loaded JSON Configuration ===")
print("Project:", loaded_config["project"])
print("Headless Mode:", loaded_config["headless"], "| Type:", type(loaded_config["headless"]))
print("Tags:", loaded_config["tags"])
