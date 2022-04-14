#returing values:
def full_name_maker(first_name, last_name, middle_name =''):
    if (middle_name):
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

name = full_name_maker("bassel","walid")
print(name)
#-------------------------------------------------------------------------------
#returing dictionaries:
def person_info_maker(first_name, last_name, age =""):
    person_info = {
        "first" : first_name,
        "last" : last_name
        }
    if age:
        person_info["ageD"] = age
    return person_info
person_sheet = person_info_maker("bassel","walid")
print(person_sheet)
