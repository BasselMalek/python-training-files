def name_greeter(names):
    """this greets the names in a list"""
    for name in names:
        msg = "hello" + " " + name.title() + "!"
        print(msg)
list = ["bassel","moe","joe"]
name_greeter(list)
