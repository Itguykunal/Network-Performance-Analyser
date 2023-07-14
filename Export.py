import json
import csv
def export_data(data, filename, file_format):
    if file_format == 'json':
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data exported to {filename} in JSON format.")
    elif file_format == 'csv':
        keys = data[0].keys()
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data exported to {filename} in CSV format.")
    else:
        print("Invalid export format.")
