import csv
with open('../sample_data/mock_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        print(', '.join(row))
