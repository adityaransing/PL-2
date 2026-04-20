import csv
import json


file_name = "data.csv"

with open(file_name, 'r') as file:
    reader = csv.reader(file)
    row_count = 0
    for row in reader:
        row_count += 1

print("Total number of rows in the CSV file:", row_count)



with open('data.json', 'r') as json_file:
    data = json.load(json_file)

with open('data.csv', 'w', newline='') as csv_file:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)