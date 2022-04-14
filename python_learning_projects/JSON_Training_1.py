import json
with open("test.json") as file_object:
    numbers = json.load(file_object)
print(numbers)
