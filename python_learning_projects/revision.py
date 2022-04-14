with open("10_1_exercise.txt") as file_object:
    lines = file_object.read()
print(lines.strip())
with open("10_1_exercise.txt") as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.strip())
with open("10_1_exercise.txt") as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.strip() + "SOLID"
    print(line)
print(lines)

with open("revision.txt","w") as target:
    for time in range(15):
        target.write("revision\n")
