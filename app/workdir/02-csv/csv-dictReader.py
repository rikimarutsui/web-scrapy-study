import csv
with open('../sample_data/mock_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        print(row['first_name'], row['last_name'])
