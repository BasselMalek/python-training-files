while True:
    response = input("Why Do You Like Programming ? ")
    if (response=="break"):
        break
    else:
        with open("10_5_exersice.txt","a") as file_object:
            file_object.write(response + "\n")
