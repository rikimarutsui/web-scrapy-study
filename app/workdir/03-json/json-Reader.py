import json
with open('../sample_data/mock_data.json', newline='') as jsonfile:
    data = json.load(jsonfile)
    # Or this way
    # data = json.loads(jsonfile.read())
    print(data)
