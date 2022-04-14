def analyzer(filename):
    """
        analyzes text in a given file, giving the number of words and,
         checks for words
    """
    active = True
    while active:
        with open(filename) as file_object:
            text = file_object.read()
            text_list = text.split()
        decide_1 = input("Do you want to know the number of words " +
            "in this file ?\n"
            )
        if (decide_1 == "yes"):
            print("It's " + str(len(text_list)) + " words long.")
        elif (decide_1 == "no"):
            print("Ok")
        decide_2 = input("Do yo
        u want to check for a word ? ")
        if (decide_2 == "yes"):
            word = input("Which word would you like to check for ? ")
            if word in text_list:
                print("It's there")
            else:
                print("It's not there")
            decide_3 = input("Do you want to check for another word ? ")
            if (decide_3 == "yes"):
                active_2 = True
                while active_2:
                    word_2 = input("what word ? ")
                    if word_2 in text_list:
                        print("It's there")
                    else:
                        print("It's not there")
                    decide_4 = input("again ? ")
                    if (decide_4 == "yes"):
                        continue
                    elif (decide_4 == "no"):
                        active_2 = False
                        print("Thank you for using this program")
                        active = False
            elif (decide_3 == "no"):
                print("Thank you for using this program")
                break
        elif (decide_2 == "no"):
            print("Thank you for using this program")
            break
analyzer("text_sample.txt")
