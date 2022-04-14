with open("name.txt") as file_object:
    name = file_object.read()
    print(name.strip())
with open('name.txt') as file_object:
    for line in file_object:
        print(line.strip() + "heh")
with open('name.txt') as file_object:
    lines = file_object.readlines()
liness =[]
for line in lines:
    new_line = line.strip()
    liness.append(new_line)
print(liness)
