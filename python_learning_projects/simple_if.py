age = 4
if (age >= 19):
    print("you can vote".title())
    print("did you vote yet ?".title())
else:
    print("you are not old enough to vote".title())

#amusement park prices :
if (age <= 4):
    print("free of charge")
elif (age <= 18):
    print("1$ per ride")
else:
    print("3$ per ride")

#personal test
john = 2
liz = 16
james = 21
family =[john,liz,james]
for member in family:
    if (member <= 4):
        price = 0
        price_1 = price
    elif (member <= 18):
        price = 1
        price_2 = price
    else:
        price = 3
        price_3 = price

print ("your total is " + str(price_1 + price_2 + price_3) + "!")
