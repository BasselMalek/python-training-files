user = {
    "first_name":"john",
    "last_name":"Johnson",
    "city":"san fransisco",
    "job":"software engineer",
    }

for x, y in user.items():
    print(x + ":")
    print("\t\t" + y)

for field in user.keys():
    print(field)

for name in user.keys():
    if (name == "first_name"):
        print(name.title())
    elif (name == "last_name"):
        print(name.title())
    else:
        print(name)
