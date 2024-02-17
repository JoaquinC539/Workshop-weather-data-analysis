[
    {
        "boardID": "X4D1YZ2D",
        "entry": "hello world"
    },
    {
        "boardID": "YEHRNZIW",
        "entry": "HELLO WORLD"
    },
    {
        "boardID": "8KRI59JD",
        "entry": "daniel"
    },
    {
        "boardID": "HEF573JF",
        "entry": "DANIEL"
    }
]
import json

# Sample dictionary
data = {'key1': 'value1', 'key2': [1, 2, 3], 'key3': {'nested_key': 'nested_value'}}

# Writing the dictionary to a JSON file
with open('example.json', 'w') as file:
    json.dump(data, file)