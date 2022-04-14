file_path = "pi.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()
print(pi_string[:5])
print(len(pi_string))
b_day = "8979"
if b_day in pi_string:
    print("P")
else:
    print("L")
