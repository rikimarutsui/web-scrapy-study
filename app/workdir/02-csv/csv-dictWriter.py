import csv
with open('../sample_data/mock_data.csv', 'a', newline='') as csvfile:
    fieldnames = ['id', 'first_name', 'last_name', 'gender', 'country']
    writer = csv.DictWriter(csvfile, fieldnames, delimiter=',', quotechar='"')
    writer.writerow({
        'id': 4,
        'first_name': 'Hello World Salvatore',
        'last_name' : 'Hello World Gaitskill',
        'gender' : 'Hello World Male',
        'country': 'Hello World Indonesia'
    })
