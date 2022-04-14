import json
test_info = input()
with open("test.json","w") as file_object:
    json.dump(test_info,file_object)
