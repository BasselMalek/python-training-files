with open('10_1_exercise.txt') as file_object:
    text = file_object.read()
print(text.strip())

with open('10_1_exercise.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())

with open("10_1_exercise.txt") as file_object:
    for line in file_object:
        print(line)
