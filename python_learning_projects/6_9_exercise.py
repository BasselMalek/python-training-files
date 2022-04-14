favorite_cities={
    "james":{
        "city_1":"denver",
        "city_2":"new york"
        },
    "liz":{
        "city_1":"denver",
        "city_2":"chicago"
        },
    "moe":{
        "city_1":"cairo",
        "city_2":"boston"
        }
    }

for person,cities in favorite_cities.items():
    print(person.title() + ":")
    for city in cities.values():
        print(city.title())
