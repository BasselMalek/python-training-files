first_name = input("what's your first name ?  ")
last_name = input("what's your last name ? ")
birth_city = input("where were you born ? ")
fav_food = input("what's your favorite food ? ")
def person_builder(first_name,last_name,birth_city,fav_food=""):
    if fav_food:
        person_info={"f_name":first_name,"l_name":last_name,"b_city":birth_city,"fv_food":fav_food}
    else:
        person_info={"f_name":first_name,"l_name":last_name,"b_city":birth_city}
    for info_field,info in person_info.items():
        print(info_field + ":\n\t" + info)


person_builder(first_name,last_name,birth_city,fav_food)
