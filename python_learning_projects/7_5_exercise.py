prompt = "Please input your age: "
while True :
    message = input(prompt)

    if (message == "end"):
        break

    if (int(message) < 3):
        print("yor ticket is free.".title())
    elif (3 <= int(message) < 12):
        print("your ticket is for $10".title())
    elif (int(message) >= 12):
        print("your ticket is for $15".title())
