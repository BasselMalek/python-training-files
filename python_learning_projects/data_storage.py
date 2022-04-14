"""Program to get user infofor further usage in other programs"""
import json
user_info = {}
print("Enter your info.")
f_name = input("First Name : ")
l_name = input("Last Name : ")
age = input("Age : ")
country = input("Country : ")
user_info["f_name"] = f_name
user_info["l_name"] = l_name
user_info["age"] = age
user_info["country"] = country
filename = "user_info.json"
with open(filename,"w") as file_object:
    json.dump(user_info,file_object)
