emotions=["chill"]
print(emotions)
emotions.append("anger")
print(emotions)
emotions.insert(0,"joy")
emotions.insert(2,"love")
print(emotions)
love=emotions.pop(2)
print(emotions)
emotions.append(love)
print(emotions)
del emotions[3]
print(emotions)
emotions.remove("joy")
print(emotions)
emotions.insert(0,love)
emotions.append("joy")
print(emotions)
print(sorted(emotions))
print(sorted(emotions,reverse=True))
emotions.reverse()
print(emotions)
emotions.reverse()
print(emotions)
emotions.sort()
print(emotions)
emotions.sort(reverse=True)
print(emotions)
print("the number of emotions in this list is " + str(len(emotions)))
