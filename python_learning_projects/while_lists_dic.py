unserved_pizzas=["veggie-pizza","cheese-mix","meat-special"]
served_pizzas=[]
while unserved_pizzas:
    in_making = unserved_pizzas.pop()
    print("Making " + in_making.title())
    served_pizzas.append(in_making)
for done in served_pizzas :
    print("Done Pizzas:\n" + done)
