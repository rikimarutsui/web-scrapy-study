import csv
with open('../sample_data/mock_data.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([3, 'Hello Corri', 'Hello Campling', 'Hello Female', 'Hello Sweden'])
