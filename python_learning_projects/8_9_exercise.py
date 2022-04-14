def magician_caller(name_list):
    for name in name_list:
        print(name)
names=["Houdini","Criss Angel","Teller"]
great_magicians = []
magician_caller(names)
#8_10 :
def greatness_giver(name_list,great_magicians):
    while name_list:
        to_be_great = name_list.pop()
        great_magician = to_be_great + " The Great"
        great_magicians.append(great_magician)
greatness_giver(names[:],great_magicians)
magician_caller(great_magicians)
#8_11:
magician_caller(names)
