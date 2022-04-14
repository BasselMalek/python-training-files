program_switch = True
print("'Input break at any point to end the program'")
while program_switch:
    file_name = input("Please input the file's location. ")
    if (file_name == ""):
        print("Please input a file path.")
    elif (file_name == "break"):
        program_switch = False
    else:
        try:
            with open(file_name) as file_object:
                file_contents = file_object.read()
        except FileNotFoundError:
            print("Invalid filepath.\nPlease input a valid file path.")
        else:
            print(file_contents.strip())
            program_switch = False
