def jump(height,unit):
    while True:
        try:
            int(height) + 1
        except ValueError:
            print("Rerun the function while entring a numerical value")
            break
        else:
            if (int(height) > 3):
                print(
                    "That's too high for me.\nPlease input a value lower than 3."
                        )
                break
            elif (int(height) < 3):
                print("I've jumped " + str(height) + unit)
                return int(height)
jump("1","M")
