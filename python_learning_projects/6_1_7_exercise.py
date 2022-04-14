James={
    "username":"james10",
    "first_name":"james",
    "last_name":"estrada",
    "city":"denver"
    }

for field, info in James.items():
    print(field.title() + ":\n\t" + info.title())

Liz={
    "username":"cutiequeen",
    "first_name":"elizabith",
    "last_name":"rogers",
    "city":"denver"
    }

Moe={
    "username":"red m&m",
    "first_name":"mohammed",
    "last_name":"ahmed",
    "city":"cairo"
    }

people=[Moe,James,Liz]
for person in people:
    print(person)
