dogs=["corgis","huskeys","pitbulls"]
print(dogs)
dogs[0]="<3 corgis"
print(dogs)
dogs.append("pugs")
print(dogs)
dogs.insert(0,"doge")
print(dogs)
del dogs[0]
print(dogs)
dogs.pop(2)
#self-discovery : putting a number in the parenthesis of pop() will remove the item with that index.
print(dogs)
some_other_dogs= dogs.pop()
print(some_other_dogs)
print("my fav dog breed is " + some_other_dogs.upper())
dogs.remove("huskeys")
print(dogs)
