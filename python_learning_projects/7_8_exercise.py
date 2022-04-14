sandwich_types = ["tuna","grilled cheese","pastrami","sausge"]
sandwich_orders = {}
print("Menu:")
for sandwich in sandwich_types:
    print(sandwich.title())

table_number = input("What's your table number ? ")
while True:
    order = input("What's your order ? ")
    x = input("wanna order again ? ")
    sandwich_orders[table_number]= orders=[]
    orders.append(order)
    if x == "yes":
        continue
    elif x == "no":
        break
print("Pick Up")
for table_number_finished,order_finished in sandwich_orders.items():
    print(table_number_finished)
    for order_1 in order_finished :
        print(order_1)
