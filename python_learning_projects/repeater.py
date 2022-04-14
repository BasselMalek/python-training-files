prompt="say something then i'll repeat it again"
prompt = prompt +"\n\tor quit and i'll kill u:\n "
#y= True
#while y:
    #x=input(prompt )
    #if (x=="quit"):
        #y = False
    #else:
        #print(x)
while True:
    x=input(prompt)
    if x == "quit":
        break
    else:
        print(x)
