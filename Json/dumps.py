import json

python_dict = {"name": "Nut", "age": 24, "city": "Chonburi"}

json_string = json.dumps(python_dict)

print(json_string)