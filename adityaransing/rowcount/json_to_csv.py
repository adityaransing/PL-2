import json
import csv

# Load JSON data
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Convert to CSV
with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write header
    writer.writerow(data[0].keys())

    # Write rows
    for item in data:
        writer.writerow(item.values())

print("JSON converted to CSV successfully!")