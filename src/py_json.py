# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample json
userJSON = '{"first_name": "John", "last_name":"doe", "age":30}'

# parse to dict
user = json.loads(userJSON)
print(user)
print(user['first_name'])

car = {'make': 'ford', 'model': 'Mustang'}
carJSON = json.dumps(car)
print(carJSON)