glossary={
    "print":"this prints the text inside or the variable's value",
    "append()":"this adds it's value to the end of a list",
    "range()":"this generates numbers ranging from the first value to the" +
    " second value",
    "pop()":"this removes an item from it's lide corresponding to it's value"
    }

for term, meaning in glossary.items():
        print(term + ":" + "\t\n" + meaning)
