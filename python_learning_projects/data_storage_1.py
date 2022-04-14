import json
with open("user_info.json") as f_obj:
    user_info = json.load(f_obj)
for key,value in user_info.items():
    print(key + " : " + value)
