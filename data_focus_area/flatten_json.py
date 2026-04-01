def flatten_json(data, parent_key='', sep='.'):
    result = {}

    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key

        if isinstance(value, dict):
            result.update(flatten_json(value, new_key, sep))
        else:
            result[new_key] = value

    return result


data = {
  "name": "John",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345"
  },
  "emails": [
    "john@example.com",
    "johnny@work.com"
  ]
}

print(flatten_json(data))