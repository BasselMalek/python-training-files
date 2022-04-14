def fav_number():
    """Greets user then prompts user for their fav number"""
    import json
    switch_1 = True
    while switch_1:
        try:
            with open("user_info.json") as user_info_file:
                user_info_dic = json.load(user_info_file)
        except FileNotFoundError:
                fav_num = input("Hello sir\nWhat's your favourite number ? ")
                with open("fav_num.json","w") as num_file:
                    json.dump(fav_num,num_file)
                switch_1 = False
        else:
            fav_num = input("Hello " + user_info_dic["f_name"].title() +
                "\nWhat's your favourite number ? ")
            with open("fav_num.json","w") as num_file:
                json.dump(fav_num,num_file)
            switch_1 = False
def rem_fav_num():
    """Use exercise_ten_eleven_moudule to remeber a user's favourite number."""
    import json
    while True:
        try:
            with open("fav_num.json") as fav_num_file:
                fav_num = json.load(fav_num_file)
        except FileNotFoundError:
            print("Info file not found.\nPlease contact support to fix this issue.")
        else:
            decide_1 = input("You want to see if I still remember your "+
                " favourite number ? ")
            if (decide_1 == "yes"):
                print("It's " + fav_num)
                break
            elif (decide_1 == "no"):
                print("I guess so.")
                break
