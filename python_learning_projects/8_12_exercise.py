def sandwich_maker(size,bread,*ingredients):
    print("Making a " + size + " " + bread + " sandwich with :")
    for ingredient in ingredients:
        print("-" + ingredient)
sandwich_maker("Huge","Toast","Tomatoes","Cheese","Ketchup")
