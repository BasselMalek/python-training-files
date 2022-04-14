polling_active = True
results={}
while polling_active:
    name = input("what's your name ?\n".title())
    response = input("what's your favourite food ?\n".title())
    results[name]=response
    confirmation = input("Again ? ")
    if confirmation == "no":
        polling_active = False
        for voter,result in results.items():
            print(voter.title() + ":" + result.title())
    elif (confirmation == "yes"):
        continue
    else:
        print("error : please input (yes/no)".title())
