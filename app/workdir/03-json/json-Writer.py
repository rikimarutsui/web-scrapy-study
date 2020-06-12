import json
with open('../sample_data/mock_data.json', newline='') as jsonfile:
    data = json.load(jsonfile)

with open('../sample_data/mock_data.json', 'w', newline='') as jsonfile:
    data.append({
        'id': 5,
        'first_name': 'First Name VIN',
        'last_name': 'Last Name STURDGESS',
        'gender': 'Gender MALE',
        'country': 'COUNTRY Greece'
    })
    json.dump(data, jsonfile)
