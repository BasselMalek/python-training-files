speeds=["slow","medium","fast"]
y = 1
x = {"height":"short",
    "face":"round",
    }
print(x["height"])
x["glasses"] = "big round"
print(x)
x["x_position"] = 0
x["y_positions"] = 0
x["speed"] = speeds[y]
#calculate the position of X
if (x["speed"]=="slow"):
    distance = 1
elif (x["speed"]=="medium"):
    distance = 2
else:
    distance = 3

x["x_position"] = x["x_position"] + distance
print(x["x_position"])
