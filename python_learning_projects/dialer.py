def phone_dialer(to_be_dialed, dialed_names):
    while to_be_dialed:
        currently_dialing = to_be_dialed.pop()
        print("Dialing" + " " + currently_dialing.title())
        print("Peeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeep")
        dialed_names.append(currently_dialing)
        if not to_be_dialed:
            for name in dialed_names:
                print(name.title() + " " + "Dialed")
user_to_be_dialed = []
dialed_names = []
while True:
    decide_1 = input("would you like to dial somebody ?\n(yes/no)")
    if (decide_1 == "yes"):
        name = input("who would you like to dial ? ".title())
        user_to_be_dialed.append(name)
        decide_2 = input("would you like to dial somebody else?\n(yes/no)")
        if (decide_2 == "yes"):
            continue
        elif (decide_2 == "no"):
            break
    elif (decide_1 == "no"):
        break
phone_dialer(user_to_be_dialed, dialed_names)
