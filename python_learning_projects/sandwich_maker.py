def sandwich_maker(size,bread,**ingredients):
    sandwich = {}
    sandwich["sizeD"] = size
    sandwich["breadD"] = bread
    for key,value in ingredients.items():
        sandwich[key] = value
    return sandwich
