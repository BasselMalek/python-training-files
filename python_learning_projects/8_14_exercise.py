def car_buyer(brand,model,**options):
    car={}
    car["car_brand"] = brand
    car["car_model"] = model
    for key, value in options.items():
        car[key] = value
    return car
print(car_buyer("ferriai","whatever",fast="yeah",sick="for sure"))
